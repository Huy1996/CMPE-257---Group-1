import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix, f1_score, roc_auc_score, roc_curve
from sklearn.model_selection import StratifiedKFold


def cross_validation(X, y, model, metrices:dict=None, k:int=5):
    """
    Perform k-fold cross-validation on the given model.

    Parameters:
    X: ndarray
        Feature metrix.
    y: ndarray
        Target vector.
    model: Object
        A machine learning model with `fit` and `predict` methods.
    k: int, optional
        Number of folds for cross-validation (default is 5).
    metrices: Dict of metric will be use
        A function to evaluate model performance
    
    Returns:
    results: list
        List of performance scores for each fold
    """

    kf = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)
    results = {key:[] for key in metrices.keys()}

    for train_index, test_index in kf.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        
        # Train model
        model.fit(X_train, y_train)
        
        # Predict on test set
        y_pred = model.predict(X_test)
        

        for key, metric in metrices.items():
            m = metric(y_test, y_pred)
            results[key].append(m)            

    return results


def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    
    # Predict on test set
    y_pred = model.predict(X_test)
    y_pred_prob = model.predict_proba(X_test)[:, 1]  # Get probability for class 1 (AUC-ROC)

    # Compute Evaluation Metrics
    auc_score = roc_auc_score(y_test, y_pred_prob)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # Print results
    print(f"🔹 AUC-ROC Score: {auc_score:.4f}")
    print(f"🔹 F1 Score: {f1:.4f}")
    print(f"📌 Confusion Matrix:\n{cm}\n")
    print(f"📌 Classification Report:\n{report}\n")

    # Plot Confusion Matrix
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    # Plot AUC-ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, color='blue', label=f'AUC = {auc_score:.2f}')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("AUC-ROC Curve")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show();

    return model
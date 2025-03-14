import numpy as np

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
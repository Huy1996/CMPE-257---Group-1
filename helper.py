import joblib
import os

def save_model(model, file_name):
    """
    Save any trained scikit-learn model using joblib.

    Parameters:
        model (Object): The trained model to save
        file_name (str): the file path to save the model
    """
    joblib.dump(model, "Models/" + file_name)
    print(f"Model saved successfully as Model/{file_name}")


def load_model(file_name):
    """
    Load a saved scikit-learn model using joblib.
    
    Parameters:
        filename (str): The file path of the saved model.
    
    Returns:
        object: The loaded scikit-learn model.
    """
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name} not found. Please train and save the model first.")
        raise FileNotFoundError(f"File '{file_name}' not found.")
    
    model = joblib.load(file_name)
    print(f"Model loaded from {file_name}")
    return model
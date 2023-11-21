import joblib

def make_predictions(X_pred, model_path):
    loaded_model = joblib.load(model_path)

    predictions = loaded_model.predict(X_pred)

    print(predictions)

    return predictions

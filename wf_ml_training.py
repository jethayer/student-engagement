import pandas as pd
import joblib

def train_model(model, model_path):
    training_data_path = 'data_processed/training_data.csv'
    train_df = pd.read_csv(training_data_path)

    X_train = train_df[['d2_rt']]
    y_train = train_df['d2_fa_rate']

    trained_model = model()

    trained_model.fit(X_train, y_train)

    joblib.dump(trained_model, model_path)

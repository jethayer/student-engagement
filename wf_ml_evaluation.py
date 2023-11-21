import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from wf_ml_prediction import make_predictions

def create_datasets():
    data_path = 'data_processed/processed_data.csv'
    df = pd.read_csv(data_path)

    df.dropna(subset=['d2_rt', 'd2_fa_rate'], inplace=True)

    X = df[['d2_rt']]
    y = df['d2_fa_rate']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if len(X_test) < 30:
        raise ValueError("Test dataset must have at least 30 samples.")

    train_data = pd.DataFrame(data=X_train, columns=X.columns)
    train_data['d2_fa_rate'] = y_train
    train_data.to_csv('data_processed/training_data.csv', index=False)

    test_data = pd.DataFrame(data=X_test, columns=X.columns)
    test_data['d2_fa_rate'] = y_test
    test_data.to_csv('data_processed/testing_data.csv', index=False)

def evaluate_model(model_path):
    joblib.load(model_path)

    test_data_path = 'data_processed/testing_data.csv'
    test_df = pd.read_csv(test_data_path)

    X_test = test_df[['d2_rt']]
    y_test = test_df['d2_fa_rate']

    y_pred = make_predictions(X_test, model_path)

    mse = mean_squared_error(y_test, y_pred)

    r2 = r2_score(y_test, y_pred)

    save_evaluation_results(model_path, mse, r2)

def save_evaluation_results(model_path, mse, r2):
    summary_path = 'evaluation/summary.txt'
    if not os.path.exists(summary_path):
        with open(summary_path, 'w') as file:
            file.write('Model\t\t                MSE\t\t                     R-squared\n')

    model_name = os.path.splitext(os.path.basename(model_path))[0]

    with open(summary_path, 'a') as file:
        file.write(f'{model_name.ljust(20)}\t\t{mse}\t\t{r2}\n')
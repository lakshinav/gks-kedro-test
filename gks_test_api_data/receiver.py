import requests
import pandas as pd
import time

if __name__ == "__main__":

    while True:
        time.sleep(5)
        # обращаемся к сайту
        response = requests.get("http://127.0.0.1:6789/arma_fit/predictor")

        # json -> DF
        df = pd.DataFrame().from_dict(response.json(), orient='index').T[[ 'index_r', 'predict_r']]
        df.columns = ['index', 'predict']

        print(df.head(1))
        # сохраняем результат
        df.to_csv('data_vault/answer.csv', mode='a', header=False, index=False)

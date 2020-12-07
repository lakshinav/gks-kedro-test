import logging
from typing import Any, Dict

import numpy as np
import pandas as pd
#from sklearn.model_selection import cross_val_score
#from sklearn import metrics


def get_api_data(data):
    return data.json()['index'], data.json()['data']['forecast_period']
           #pd.DataFrame.from_dict(data.json()['data'], orient='index').T


def make_prediction(n, pred_num, model):
    # импорты в функции

    predict = model.predict(n+pred_num, n+pred_num)

    return predict


def serve_result(row_index, predict):
    """
    answer = {"predict_date": _90.headers['date'],
              "row_index": _90.json()['index'],
              "predict": float(rf_model.predict(df))
              }
    """

    return row_index, float(predict) if len(predict) == 1 else list(predict)


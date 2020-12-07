from kedro.pipeline import Pipeline, node

from .nodes import *


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                get_api_data,
                "api_data",
                ["index", "predict_num"]
            ),
            node(
                make_prediction,
                ["tot_length", "predict_num", "arma_fit"],
                "predict"
            ),
            node(
                serve_result,
                ["index", "predict"],
                ["index_r", "predict_r"]
            )
        ]
    )

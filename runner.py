import uvicorn
from fastapi import FastAPI
#import numpy as np
#import pandas as pd

from kedro.framework.context import load_context
#from kedro.extras.datasets.api import APIDataSet
from src.gks_test.pipelines.api_pipeline import pipeline
#import json


app = FastAPI()
@app.post("/{model}/predictor") # if get, you'll see the result on arma_fit/predictor web site; if post, you won't see it on the web-site, but can see in request tester on /docs
async def predictor(model):
    if model == 'arma_fit':
        context = load_context("")
        output = context.run(pipeline_name='api_pipeline')

    return output



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=6789)

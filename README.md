# gks-kedro-test
Repo for "ML in production" course at HSE, branch for deployment code.
Course [repo](https://github.com/NameArtem/deployml_course).
This project is on Python 3.8, kedro 0.16.6.
Below `./` is the project folder.

The whole project includes the following steps:
0. Setup kedro project
  0.1 `kedro new` in terminal
  0.2 Write all needed libraries to ./src/requirements.in and `pip-compile .src/requirements.in` in terminal; you'll get ./src/requirements.txt
  0.3 `kedro install` in terminal; all the dependencies will turn up in kedro environment (../lib)
1. Take a notebook and convert it to kedro nodes and pipelines. The pipelines include DE and DS. The changes touch:
  1.1 ./src/project_name/: nodes and pipelines (one pipeline = one folder)
  1.2 ./data and ./conf/base/catalog.yml: datasets used in pipelines
  1.3 ./conf/base/parameters.yml: constant values in nodes and pipelines
2. Add API to communicate model predictions
  2.1 Add pipeline for prediction
  2.2 Add pipeline for getting data from server, predict and sent (API pipeline)
  2.3 Don't forget to add new pipelines to ./src/project_name/hooks.py
  2.4 Create data vault with 
    2.4.1 data, which are sent to model for prediction
    2.4.2 file, where these data are saved
    2.4.2 file, where predictions are saved
  2.5 In data vault create server app, which send data to 127.0.0.1/9876/data (post or get) and save them to file 2.4.2
  2.6 Create ./runner.py, which get data from 127.0.0.1/9876/data and send it to prediction pipeline 2.1
  2.7 In data vault create receiver.py, which send the request (post or get, the same as in 2.5) to 
    
    
    
    server add, which 

1. Define and install dependencies.
We use [poetry](https://python-poetry.org/) to resolve dependencies and create `requirements.txt` file.
```bash
$ poetry init # create just pyproject.toml w/o project folder structure
$
```

2. Run nginx and serv_app.py on it to serve data to the model (arma_fit).

```bash
$ sudo docker container run -p 80:80 nginx
```

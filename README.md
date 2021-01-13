# gks-kedro-test

Repo for "ML in production" course at HSE, branch for deployment code.
Course [repo](https://github.com/NameArtem/deployml_course).
This project is on Python 3.8, kedro 0.16.6.
Below `./` is the project folder.

# Walkthrough

The whole project includes the following steps:

0. Setup kedro project

  0.0 `source bin/activate` in terminal to activate kedro environment
  
  0.1 `kedro new` in terminal
  
  0.2 Write all needed libraries to ./src/requirements.in and `pip-compile .src/requirements.in` in terminal; you'll get ./src/requirements.txt
  
  0.3 `kedro install` in terminal; all the dependencies will turn up in kedro environment (../lib)

1. Take a notebook and convert it to kedro nodes and pipelines. The pipelines include DE and DS. The changes touch:
  
  1.1 ./src/project_name/: nodes and pipelines (one pipeline = one folder)
  
  1.2 ./data and ./conf/base/catalog.yml: datasets used in pipelines
  
  1.3 ./conf/base/parameters.yml: constant values in nodes and pipelines
  
  1.4 If you need the project graph, `kedro viz` in terminal; the scheme will be on 127.0.0.1:4141

2. Add API to communicate model predictions (based on FastAPI and uvicorn)
  
  2.1 Add pipeline for prediction
  
  2.2 Add pipeline for getting data from server, predict and sent to port 6789 (API pipeline)
  
  2.3 Don't forget to add new pipelines to ./src/project_name/hooks.py
  
  2.4 Create data vault with 
    
    2.4.1 data, which are sent to model for prediction
    
    2.4.2 file, where these data are saved
    
    2.4.3 file, where predictions are saved
  
  2.5 In data vault create server app, which send data to 127.0.0.1/9876/data (post or get) and save them to file 2.4.2
  
  2.6 Create ./runner.py, which get data from 127.0.0.1/9876/data, pass it to prediction pipeline 2.1 and send to 0.0.0.0:6789/<model_name>/predictor
  
  2.7 In data vault create receiver.py, which send the request (post or get, the same as in 2.5) to 127.0.0.1:6789/<model_name>/predictor, get prediction and save it to file 2.4.3
  
  2.8 Run API:
    
    2.8.1 `cd` to data vault, `python server_app.py` in terminal
    
    2.8.2 open new tab in terminal, activate kedro environment, `cd` to project folder and `python runner.py` in terminal
    
    2.8.3 open new tab in terminal, activate kedro environment, `cd` to data vault, `python receiver.py` in terminal
  
  2.9 Check API
  
    2.9.1 Go to 127.0.0.1:9876/data and you should see data from 2.4.1
    
    2.9.2 Go to 127.0.0.1:6789/doc and try to request prediction (if it's post, not get)
    
    2.9.3 If everything is ok, you'll see predictions in data vault, in file 2.4.3

3. Testing
  
  3.1 Write tests in ./src/tests; use `hypothesis`
  
  3.2 Run `kedro test` and see the testing results and coverage
  
  3.3 If you need coverage report: `kedro test --cov=src --verbose`; `.coverage` file appears in ./
  
  3.4 If you need report in html: `kedro test --html=report.html --self-contained-html`; `report.html` file appears in ./

4. Github actions

  4.1 dependabolt
  
  4.2 MissPell
  
  4.3 tests
  
  4.4 codecov
  
5. Docker
  
    
    
    
If you need particular version of python to run kedro, you can use `venv` to create envinronment and `poetry` to install dependencies.

1. Define command for the python version needed: `$ alias python3.8 pold` 

1. Create env for python 3.8: `$ pold -m venv kedro_env`

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

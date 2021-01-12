# gks-kedro-test
Repo for "ML in production" course at HSE, branch for deployment code.
Course [repo](https://github.com/NameArtem/deployml_course).

Step by step:

1. Define and install dependencies.
We use [poetry](https://python-poetry.org/) to resolve dependencies and create `requirements.txt` file.
> $ poetry init # create just pyproject.toml w/o project folder structure
> $ 

2. Run nginx and serv_app.py on it to serve data to the model (arma_fit).

> sudo docker container run -p 80:80 nginx

# DBS Assignment Example in Python

This repository is a simple example of a Python HTTP application based on the [FastAPI](https://fastapi.tiangolo.com/)
containerized in the Docker environment. You don't have to stick with the FastAPI for your assignments, this repository
is just a simple example of Docker build process with environments variables (which you have to use because of the
database configuration).

If you have any questions feel free to create a issue or offer a pull request.

## Content of the repository

Application contains a simple HTTP endpoint `GET /v1/hello` which will return a JSON bellow where value of the `hello`
property is from the `NAME` environment variable. Environment variables are processed using the
[BaseSettings](https://docs.pydantic.dev/usage/settings/) object of the [pydantic](https://docs.pydantic.dev/) library.

`Dockerfile` inside the repository contains all required dependencies for the Python PostgreSQL driver
[psycopg2-binary](https://pypi.org/project/psycopg2-binary/). If you want to build a `psycopg2` from source (using the
[psycopg2](https://pypi.org/project/psycopg2/) you have to install a compiler inside the container).

The `.github/workflows/publish.yml` contains a CI/CD configuration for the Docker image build and publish using the
GitHub Actions. If you wish to build and publish the image manually check the installation section specialized for the
Docker image.

## Structure

- `.github/workflows/publish.yml`: GitHub Action recipe for Docker build and publish to the GitHub Container Registry
(you probably don't need to touch this)
- `dbs_assignment`: application module
  - `endpoints`: module for HTTP endpoints
    - `hello.py`: home of the `GET /v1/hello` HTTP endpoint
  - `__init__.py`: Check Python [docs](https://docs.python.org/3/tutorial/modules.html#packages)
  - `__main__.py`: Check Python [docs](https://docs.python.org/3/library/__main__.html)
  - `config.py`: Definition of the settings object
  - `router.py`: FastAPI [router](https://fastapi.tiangolo.com/tutorial/bigger-applications/?h=#apirouter)
- `.dockerignore`: Files skipped in the Docker `COPY` command
- `.editorconfig`: Nice & shiny editor settings
- `.gitignore`: Files ignored by git
- `Dockerfile`: Docker image definition
- `requirements.txt`: Python [dependencies file](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

## Installation

### From source

These are instructions for Linux/macOS operating systems. Windows may differ depending on your system configuration.
Keep in mind that application requires to have present variables from the `config.py`. Check the Pydantic docs provided
for more information.

1. Create python virtual environment: `python -m venv venv`
2. Enter environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run application: `uvicorn dbs_assignment.__main__:app --reload`

### Docker

You can build your Docker image with name dbs-example simply by calling:

```shell
docker build -t dbs-example .
```

After successfully build, you can run it as a container named `dbs-example-container` using command bellow.
This example also pass the `NAME` environment variable with value `Dexter` and redirect ports, so you can access the
HTTP server inside the container.

```shell
docker run -p 127.0.0.1:8000:8000 --env NAME=Dexter --name dbs-example-container dbs-example
```

---
![](docs/fiit.png)

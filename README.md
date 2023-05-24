# Taxi demand predictor service

## Setup Tools

### Install Pyenv

```bash
$ curl https://pyenv.run | bash
```
*remember to follow any additional required steps through installation.*

### Install Python 3.9

```bash
$ pyenv install 3.9.16
$ pyenv global 3.9.16
```

### Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
*remember to follow any additional required steps through installation.*


## Initial Development Setup

Create the folder project `taxi_demand_predictor` with the python package `src` within it

```bash
$ poetry new taxi_demand_predictor --name scr
$ cd taxi_demand_predictor
```

Activate the environment
```bash
$ poetry shell
```

Install the `src` package
```bash
$ poetry install
```

## Create the notebooks folder

```bash
$ mkdir notebooks
```

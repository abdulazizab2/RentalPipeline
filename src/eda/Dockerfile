FROM python:3.8-slim-buster

RUN apt-get update

RUN pip install --no-cache-dir \
    pandas==1.2.3 \
    ydata-profiling==4.2.0 \
    jupyterlab==3.0.12 \
    notebook==6.4.4 \
    wandb==0.13.5 \
    seaborn==0.11.1 \
    pyarrow==2.0 \
    notebook==6.4.4

ARG WANDB_PROJECT
ENV WANDB_PROJECT=$WANDB_PROJECT

EXPOSE 8888

WORKDIR /mlflow/projects/code

FROM python:3.8-slim-buster

RUN apt-get update
RUN pip install --no-cache-dir \
    pandas==1.2.3 \
    wandb==0.15.3 \
    mlflow==2.3.1 \
    scikit-learn==0.24.1 \
    matplotlib==3.2.2 \
    pillow==8.1.2

ARG WANDB_PROJECT
ARG WANDB_RUN_GROUP
ENV WANDB_PROJECT=$WANDB_PROJECT
ENV WANDB_RUN_GROUP=$WANDB_RUN_GROUP

WORKDIR /mlflow/projects/code
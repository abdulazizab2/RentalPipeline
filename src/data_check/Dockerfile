FROM python:3.8-slim-buster

RUN apt-get update
RUN pip install --no-cache-dir \
    pandas==1.2.3 \
    wandb==0.15.3 \
    pytest==6.2.2 \
    scipy==1.5.2

ARG WANDB_PROJECT
ARG WANDB_RUN_GROUP
ENV WANDB_PROJECT=$WANDB_PROJECT
ENV WANDB_RUN_GROUP=$WANDB_RUN_GROUP

WORKDIR /mlflow/projects/code
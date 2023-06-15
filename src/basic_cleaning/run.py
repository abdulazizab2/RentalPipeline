#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import os
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(project=os.getenv("WANDB_PROJECT"),
                     group=os.getenv("WANDB_RUN_GROUP"), job_type="basic_cleaning")
    run.config.update(args)

    logger.info(f"fetching {args.input_artifact} dataset from artifact store")
    artifact_path = run.use_artifact(args.input_artifact).file()

    df = pd.read_csv(artifact_path)
    idx = df['price'].between(args.min_price, args.max_price)
    df = df[idx].copy()
    df['last_review'] = pd.to_datetime(df['last_review'])
    df.to_csv(args.output_artifact)

    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(args.output_artifact)
    run.log_artifact(artifact)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="input raw data artifact to perform data cleaning",
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="output cleaned data artifact",
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="type of output data",
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="cleaned and preprocessed data",
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="minimum price of a property, records with lower than min price will be dropped.",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="maximum price of a property, records with higher than max price will be dropped.",
        required=True
    )

    args = parser.parse_args()

    go(args)

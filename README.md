# ML Pipeline for Short-Term Rental Prices in NYC
You are working for a property management company renting rooms and properties for short periods of 
time on various rental platforms. You need to estimate the typical price for a given property based 
on the price of similar properties. Your company receives new data in bulk every week. The model needs 
to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

# Links
[Project Link](https://github.com/abdulazizab2/RentalPipeline)
[Training and pipeline logs](https://wandb.ai/abdulazizab/nyc_airbnb?workspace=user-abdulazizab)
# Requirements

- [Docker](https://docs.docker.com/engine/install/)
- [wandb](wandb.ai) API key

## Optional - Development requirements

```bash
pip install -r requirements.txt
```

# Pipeline Execution

1. Build all images
```bash
docker compose build --build-arg WANDB_PROJECT=nyc_airbnb --build-arg WANDB_RUN_GROUP=development
```
2. Export your wandb API key
```bash
export WANDB_API_KEY=${YOUR_WANDB_API_KEY}
```
# License

[License](LICENSE.txt)

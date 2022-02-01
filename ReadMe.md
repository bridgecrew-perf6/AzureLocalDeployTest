## About

The repository can be used as reference to deploy machine learning model on local machine using Azure services.
With a few changes, this can be turned into a production environment and deployed on Azure Machine Learning.

The approach is time saving i.e. without setting up API, server, gunicorn, writing extra code and so on.

Docker needs to installed and an Azure account with Subscription and Resource Group should be available.


## Ensure the config file is correct.

The config file can be download from Azure portal or created as below.

```
{
    "subscription_id": "subscription id --not name but id",
    "resource_group": "Resource group name",
    "workspace_name": "Workspace name"
}
```

## Register the Model

Even though the model will be deployed on local docker machine, it needs to be registered.
A trained pickle file should be registered, example in `ModelRegister.py`.

A pickles example can be generated from `train.py`.

## Create Env file

Add relevant dependencies in `env.yml` file.

## Deploy the model, ensure local deployment

Once model is registered. Deploy on docker machine. Example script `ModelDeploy.py`.
For production purpose, change the `deployment_config` and set appropriate `Webservice`.

## Prepare score file

The `score.py` is a example that is required.
The `init` & `run` functions are required.

## Deploy

Run the `ModelDeploy.py` script. It may take some time.
The deploymeny url endpoint will be printed at the end.

## Test Deployment
Data supplied should be in a json format with title as `data`.
An example is `testDeploy.py`


## Finally don't forgot to delete the resources on portal.azure.com

Clean up Azure resource as required.

## Share docker setup

`docker save lmmodel > lmmodel.tar`

transfer this tar file on different machine and `docker load < lmmodel.tar`

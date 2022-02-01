## Ensure the config file is correct.


## Register the Model
This may be skipped, need to test


## Deploy the model, ensure local deployment


## while scoring ensure to add data paramter

The score.py run command needs a type of structure.

'{"data": [' + str(df.to_dict()) + ']}'

## Finally don't forgot to delete the resources on portal.azure.com

End points incur cost

## save the docker image on local machine 

docker save lmmodel > lmmodel.tar

transfer this tar file on different machine and docker load < lmmodel.tar
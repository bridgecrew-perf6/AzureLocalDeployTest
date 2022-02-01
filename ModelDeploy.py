from azureml.core.webservice import Webservice, LocalWebservice
from azureml.core.model import InferenceConfig
from azureml.core.environment import Environment
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core import Workspace
from azureml.core.model import Model

ws = Workspace.from_config()
# Workspace.get(name="myworkspace", subscription_id='<azure-subscription-id>', resource_group='myresourcegroup')
model = Model(ws, 'LinearModel') #No need to register we can directly assign the pickle file?

myenv = Environment.from_conda_specification(name='sklearn-env', file_path='env.yml')

# myenv = Environment.get(workspace=ws, name="tutorial-env", version="1")


inference_config = InferenceConfig(entry_script="score.py", environment=myenv)

deployment_config = LocalWebservice.deploy_configuration(port=6789)

# Azure deploy
# dep_config = AciWebservice.deploy_configuration(cpu_cores = 1,
#                                                 memory_gb = 1,
#                                                 enable_app_insights=True)

localservice = Model.deploy(workspace=ws, 
                       name='lmmodel', 
                       models=[model], 
                       inference_config=inference_config, 
                       deployment_config = deployment_config)

localservice.wait_for_deployment(show_output=True)
print(f"Scoring URI is : {localservice.scoring_uri}")
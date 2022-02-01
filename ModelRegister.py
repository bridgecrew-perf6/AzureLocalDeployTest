from azureml.core.model import Model
from azureml.core import Workspace

#No need to register we can directly assign the pickle file?
# As the Deploy code downloads the pickle file again.

ws = Workspace.from_config()

model = Model.register(model_path="LinearModel.pkl",
                       model_name="LinearModel",
                       tags={'area': "temp", 'type': "regression"},
                       description="test",
                       workspace=ws)
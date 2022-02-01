# send raw HTTP request to test the web service.
import requests
import pandas as pd
import numpy as np


# preddata = pd.DataFrame({"bias":[1], "X": [5]})
# preddata = np.array([1,5]).reshape(1,-1)
# input_data = '{\"data\": ' + str(df.to_dict(orient='records')) + '}'

# input_data = "{\"data\": [" + str(preddata) + "]}"
input_data = "{\"data\": [[1, 7]]}"

headers = {"Content-Type": "application/json"}

scoring_uri = "http://localhost:6789/score"
resp = requests.post(scoring_uri, input_data, headers=headers)

print("POST to url", scoring_uri)
print("prediction:", resp.text)
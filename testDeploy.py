# send raw HTTP request to test the web service.
import requests
import pandas as pd
import numpy as np

# For dataframe input
preddf = pd.DataFrame({"bias":[1,1], "X": [5,7]})
input_data = "{\"data\": " + str(preddf.values.tolist()) + "}"

# One input
# input_data = "{\"data\": [[1, 7]]}"
# Two rows 1,7 & 1,5
#input_data = "{\"data\": [ [1, 7], [1, 5] ]}"

headers = {"Content-Type": "application/json"}

scoring_uri = "http://localhost:6789/score"
resp = requests.post(scoring_uri, input_data, headers=headers)

print("POST to url", scoring_uri)
print("prediction:", resp.text)
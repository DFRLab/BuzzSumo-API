# -*- coding: utf-8 -*-

# import modules
import pandas as pd
import requests
import json
import os

# bar progress
from tqdm import tqdm


# load API KEY
api_key_path = os.path.abspath('../config/api_key.json')
with open(api_key_path) as auth:
    api_key = json.load(auth)['api_key']
    auth.close()

# load parameters
params_path = os.path.abspath('./endpoints/articles.json')
with open(params_path) as file:
    params = json.load(file)
    file.close()

# parameters
params['api_key'] = api_key
URL = params['url']

# deleting URL key -> This will be used as variable instead.
del params['url']

# request
req = requests.request(method='GET', url=URL, params=params)
results = req.json()

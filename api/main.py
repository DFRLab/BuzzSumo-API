# -*- coding: utf-8 -*-

# import modules
import pandas as pd
import requests
import json
import os

# load API KEY
path = os.path.abspath('../config/api_key.json')
with open(path) as auth:
    api_key = json.load(auth)['api_key']
    auth.close()

# load parameters

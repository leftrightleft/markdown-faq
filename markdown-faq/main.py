#!/usr/bin/python

import os
import json
 
# printing environment variables
# print("printing env vars")
# context = json.dumps(os.environ)
print(os.environ['action'])
print(os.environ['created_at'])
print(os.environ['updated_at'])
print(os.environ['login'])
print(os.environ['body'])
#!/usr/bin/python

import os
import json
 
# printing environment variables
# print("printing env vars")
# context = json.dumps(os.environ)
body = '''---
title: {}
version: 1.0
datetime:
  draft: {}
  published: {}
catagories:
  - Internal
  - External
owners:
  - GeekMasher
  - alonahlobina
  - adityasharad
---
## {}
{}
'''.format(os.environ['title'],
        os.environ['created_at'], 
        os.environ['updated_at'], 
        os.environ['title'], 
        os.environ['body'])
# print('action', os.environ['action'])
# print('created', os.environ['created_at'])
# print('updated', os.environ['updated_at'])
# print('login', os.environ['login'])
# print('body', os.environ['body'])

f = open("demofile2.md", "w")
f.write(body)
f.close()
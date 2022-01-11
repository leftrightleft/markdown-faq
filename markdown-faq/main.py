#!/usr/bin/python

import os
import json
 
# printing environment variables
# print("printing env vars")
# context = json.dumps(os.environ)
frontmatter = '''
---
action: {}
created: {}
updated: {}
---
'''
print('action', os.environ['action'])
print('created', os.environ['created_at'])
print('updated', os.environ['updated_at'])
print('login', os.environ['login'])
print('body', os.environ['body'])

f = open("demofile2.md", "a")
f.write(frontmatter, os.environ['body'])
f.close()
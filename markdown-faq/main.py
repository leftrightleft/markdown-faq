#!/usr/bin/python

import os
from string import Template
import yaml


def get_tags():
    print(os.environ['body'])
    tags_string = os.environ['body'].split("### Tags\n\n",1)[1]
    tags = tags_string.split(',')
    tags = {'tags':[x.strip(' ') for x in tags]}
    formatted_tags = yaml.dump(tags, default_flow_style=False)
    return formatted_tags

def main():
    tags = get_tags()
    with open('/markdown-faq/template.txt', 'r') as f:
        src = Template(f.read())
        result = src.substitute(os.environ, tags=tags)

    f = open(os.environ['title'] + ".md", "w")
    f.write(result)
    f.close()

if __name__ == '__main__':
    main()

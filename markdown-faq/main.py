#!/usr/bin/python

import os
from string import Template
import yaml


def get_tags():
    tags_string = os.environ['body'].split("### Tags\n\n",1)[1]
    if len(tags_string) == 0:
        return 
    tags = tags_string.split(',')
    tags = {'tags':[x.strip(' ') for x in tags]}
    formatted_tags = yaml.dump(tags, default_flow_style=False)
    return formatted_tags

def main():
    tags = get_tags()
    directory = os.environ['directory'].strip('/')

    with open('/markdown-faq/template.txt', 'r') as f:
        src = Template(f.read())
        result = src.substitute(os.environ, tags=tags)

    isExist = os.path.exists(directory)
    if not isExist:
        os.makedirs(directory)

    f = open('{}/{}.md'.format(directory, os.environ['title']), "w")
    f.write(result)
    f.close()

if __name__ == '__main__':
    main()

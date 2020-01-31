#!/usr/bin/env python
import datetime
import json

import yaml
from jsonschema.compat import (
    Sequence,
    int_types,
    iteritems,
    lru_cache,
    str_types,
    unquote,
    urldefrag,
    urljoin,
    urlopen,
    urlsplit,
)

def coalesce(obj, *arg):
    for el in arg:
        val = obj.get(el, None)
        if val:
            return val
    return ""

def resolve_ref(ref):
    file, path = urldefrag(ref)
    data = read_yaml(file)
    if len(path) > 0:
        for path in path.split('/'):
            data = data[int(path)] if path.isdigit() else data[path]
    return data

def dump(data):

    def datetime_formatter(o):
        if type(o) is datetime.date or type(o) is datetime.datetime:
            return o.strftime("%Y-%b-%d")
#    return yaml.dump(data)
    return json.dumps(data, indent=2, default=datetime_formatter)

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def tab_indent(content_length, left_margin=80, tab_length=8):
    import math
    tabs = math.floor((left_margin - content_length - 1) / tab_length)
    return '\t' * tabs


class CV:

    cv_data = None
    yaml_file = None

    def __init__(self, file_name):
        """ constructor.
        """
        if self.yaml_file or not self.cv_data:
            self.cv_data = self.parse_file(file_name)
        
    def parse_file(self, file_name):
        """
        """
        with open("../data/" + file_name, "r") as f:
            return yaml.safe_load(f)
        return None

    def dump(self):
        json.dumps(self.cv_data, indent=2, default=datetime_formatter)

    def definitions():
        return self.parse_file('definitions')

    def training():
        return self.parse_file('training')


if __name__ == "__main__":
    print(help(yaml))

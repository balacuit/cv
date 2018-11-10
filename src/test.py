#!/usr/bin/env python

import datetime
import json
import yaml

def default(o):
  if type(o) is datetime.date or type(o) is datetime.datetime:
    return o.strftime("%Y-%b-%d")

file_name = "../data/definitions"
file_name = "../data/companies"
#file_name = "resume.yaml"
with open(file_name, "r") as f:
    dataMap = yaml.safe_load(f)

print(json.dumps(dataMap, indent=2, default=default))

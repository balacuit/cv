#!/usr/bin/env python

import datetime
import json
import yaml

def coalesce(*arg):
  for el in arg:
    if el is not None:
      return el
  return None

def datetime_formatter(o):
  if type(o) is datetime.date or type(o) is datetime.datetime:
    return o.strftime("%Y-%b-%d")

def read_yaml(file):
	with open("../data/" + file, "r") as f:
		return yaml.safe_load(f)

def dump(data):
	json.dumps(data, indent=2, default=datetime_formatter)

def report_awards():
	data = read_yaml('awards')

	print("## {}\n".format(data['title']))

	awards = data['entries']
	awards.sort(key=lambda i:i['dated'], reverse=True)

	for award in awards:

		type = award['type']
		if award['type'] == 'Bonus Award': 	# be more specific
			award['category']

	 	print("{} ({}){}{}".format(
	 			type,
				award['dated'].strftime("%Y"),
				'\t' * ((32 - len(type)) / 8),
				award.get('summary', award.get('team', award.get('category')))
	 		))

def report_definitions():
	definitions = read_yaml('definitions')




report_definitions()

report_awards()


#!/usr/bin/env python
from textwrap import TextWrapper
import textwrap

from datetime import datetime
from utils import (CV, coalesce, dump, read_yaml, tab_indent)

tw = TextWrapper(width=90)
def report_projects():
    data = read_yaml('../data/projects')
    projects = data['entries']
    projects.sort(key=lambda i: i.get('start', datetime.today()), reverse=True)

    company = ""
    for project in projects:
        if company != project['company']:
            company = project['company']
            print("\n{}".format(company))
        row = {
            'company': project.get('company', ''),
            'role': project.get('role', ''),
            'range': project.get('start', None).strftime('%Y/%b'),
            'summary': tw.fill(project.get('summary', '').strip()),
        }
        if project.get('end', None):
            row['range'] += " - " + project['end'].strftime('%Y/%b')
        else:
            row['range'] += " - present"

        row['indent'] = tab_indent(len(row['role']), left_margin=68,)
        print("\n{role}{indent}{range}\n{summary}\n"
                .format(**row))
        for task in project.get('tasks', []):
            print(textwrap.fill(task['task'],
                                initial_indent="- ",
                                subsequent_indent="  ",
                                width=80,))

def report_awards():
    data = read_yaml('../data/awards')

    print("\n\n## {}\n".format(data['about']))

    awards = data['entries']
    awards.sort(key=lambda i:i['dated'], reverse=True)

    for award in awards:

        type = award['type']
        if award['type'] == 'Bonus Award':     # be more specific
            award['category']
        row = {
            'type': type,
            'date': award['dated'].strftime("%Y"),
            'indent': tab_indent(len(type), left_margin=32),
            'summary': coalesce(award, 'summary', 'team', 'category'),
        }
        print("{type} ({date}){indent}{summary}"
            .format(**row))



def report_training():
    data = read_yaml('../data/training')

    print("\n\n## {}\n".format(data['about']))

    training = data['entries']
    training.sort(key=lambda i:i['date'], reverse=True)

    for training in training:
        row = {
            'type': training['title'],
            'date': training['date'].strftime("%Y"),
            'summary': coalesce(training, 'subtitle', 'category'),
        }
        row['indent'] = tab_indent(len(row['type']))
        print("{type}{indent}{date}\t\n    {summary}"
            .format(**row))




if __name__ == "__main__":
    report_projects()
    report_awards()
    report_training()

#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    userid = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userid))
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = userid + '.csv'
    with open(filename, mode='w') as f:
        writist = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userid):
                writist.writerow([userid, name, str(task.get('completed')),
                                 task.get('title')])
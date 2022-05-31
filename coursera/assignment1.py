import re
import numpy as np

"""
Part A
Find a list of all of the names in the following string using regex.
"""


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    names = re.findall("[A-Z]\S*\w", simple_string)
    return names


assert len(names()) == 4, "There are four names in the simple_string"

" Part B"
"""The dataset file in assets/grades.txt contains a line separated list of 
people with their grade in a class. Create a regex to generate a list of 
just those students who received a B in the course. 
"""


def grades():
    grades = []
    with open("assets/grades.txt", "r") as file:
        grades_file = file.read()
    for line in grades_file.split('\n'):
        if re.search("B$|B $", line):
            name = re.match("^[^:]*", line)
            grades.append(name.group())
    return grades


assert len(grades()) == 16

"Part C"
"""
Consider the standard web log file in assets/logdata.txt. This file records
the access a user makes when visiting a web page (like this one!).
Each line of the log has the following items: a host (e.g., '146.204.224.152')
a user_name (e.g., 'feest6811' note: sometimes the user name is missing!
In this case, use '-' as the value for the username.)
the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
example_dict = {"host":"146.204.224.152",
                "user_name":"feest6811",
                "time":"21/Jun/2019:15:45:24 -0700",
                "request":"POST /incentivize HTTP/1.1"}
"""


def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()

    # YOUR CODE HERE
    logs = []
    for line in logdata.split('\n'):
        line_dict = {}
        if line == "":
            pass
        else:
            host = re.search("^[^ ]*", line)
            line_dict["host"] = host.group()
            user_name = re.search(".*- (.*) \[", line)
            line_dict["user_name"] = user_name.group(1)
            time = re.search("^.*\[(.*)\].*$", line)
            line_dict["time"] = time.group(1)
            request = re.search(".*\"(.*)\"", line)
            line_dict["request"] = request.group(1)

            logs.append(line_dict)
    return logs


assert len(logs()) == 979
one_item = {'host': '146.204.224.152',
            'user_name': 'feest6811',
            'time': '21/Jun/2019:15:45:24 -0700',
            'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
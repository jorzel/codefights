"""
You are given a list of API calls in the format /project/subproject/method. You need to calculate and print the number of calls to each node of the API endpoint as a tree.

In this tree, projects, subprojects, and methods should be sorted in the same order as they were given in the input data. The output tree should consist of several strings. All subprojects fall under their parent project, and all methods fall under the subproject in which they are included. The string that represents a project starts with --, while subprojects start with ---- and methods start with ------. After the project, subproject, or method name, put the number of requests to this module in parentheses. Take a look at the example for a guide of what this tree should look like.

Example

For

calls = [
        "/project1/subproject1/method1",
        "/project2/subproject1/method1",
        "/project1/subproject1/method1",
        "/project1/subproject2/method1",
        "/project1/subproject1/method2",
        "/project1/subproject2/method1",
        "/project2/subproject1/method1",
        "/project1/subproject2/method1"
]
the output should be

countAPI(calls) = [
        "--project1 (6)",
        "----subproject1 (3)",
        "------method1 (2)",
        "------method2 (1)",
        "----subproject2 (3)",
        "------method1 (3)",
        "--project2 (2)",
        "----subproject1 (2)",
        "------method1 (2)"
]
Here, the first mention of project2 was after the first mention of project1, so project1 comes first. In the same way, the first mention of /project1/subproject1 comes before /project1/subproject2, so it comes first in the output.
"""


from collections import OrderedDict

def count_folders(folder, d, depth):
    if folder not in d:
        d[folder] = OrderedDict()
        d[folder]['count'] = 1
        d[folder]['depth'] = depth
    else:
        d[folder]['count'] += 1

def append_folders(folders, l):
    for f, content in folders:
        l.append(content['depth'] * '--' + f + ' (' + str(content['count']) + ')')
        del content['count']
        del content['depth']
        if content is not None:
            append_folders(content.items(), l)


def countAPI(calls):
    d = OrderedDict()
    l = []
    for c in calls:
        f = c.split('/')
        subd = d
        for i, x in enumerate(f):
            if i == 0:
                continue
            count_folders(f[i], subd, i)
            subd = subd[f[i]]
    append_folders(d.items(), l)
    return l


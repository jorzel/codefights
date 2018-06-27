"""
Asana is exploring a smart-workload feature designed to streamline task assignment between coworkers. Newly created tasks will be automatically assigned to the team member with the lightest workload. For the ith person, the following information is known:

namesi - their name, a string containing only uppercase and lowercase letters;
statusesi - their vacation indicator status, which is true if the person is on a vacation, or false otherwise;
projectsi - the number of projects they are currently involved in;
tasksi - the number of tasks assigned to them.
If a person's vacation indicator value is set to true, this means they are on vacation and cannot be assigned new tasks. Conversely, a vacation indicator value of false means they are open to receive task assignments.

Asana sorts team members according to their availability. Person A has a higher availability than person B if they have fewer tasks to do than B, or if these numbers are equal but A has fewer assigned projects than B. Put another way, we can say that person A has a higher availability than person B if their (tasks, projects) pair is less than the same pair for B.

Your task is to find the name of the person with the highest availability. It is guaranteed that there is exactly one such person.

Example

For names = ["John", "Martin"], statuses = [false, false],
projects = [2, 1] and tasks = [16, 5],
the output should be
smartAssigning(names, statuses, projects, tasks) = "Martin".

The arguments represent information about two team members:

"John", with status = false, projects = 2 and tasks = 16;
"Martin", with status = false, projects = 1 and tasks = 5.
Here John and Martin's vacation indicators are both false, so both of them are open to new assignments. Martin is only assigned 5 tasks while John is assigned 16, so Martin has the highest availability.

For names = ["John", "Martin"], statuses = [false, true],
projects = [2, 1] and tasks = [6, 5],
the output should be
smartAssigning(names, statuses, projects, tasks) = "John".

The arguments stand for the following team members:

"John", with status = false, projects = 2 and tasks = 1;
"Martin", with status = true, projects = 1 and tasks = 5.
In this example Martin cannot be assigned any new tasks because his vacation indicator is true. Therefore, "John" has the highest availability.

For names = ["John", "Martin"], statuses = [false, false],
projects = [1, 2] and tasks = [6, 6],
the output should be
smartAssigning(names, statuses, projects, tasks) = "John".

In this case:

"John", with status = false, projects = 1 and tasks = 6;
"Martin", with status = false, projects = 2 and tasks = 6.
Both John and Martin's vacation indicators are false, and the number of tasks each of them is assigned is 6. However, John is only involved in 1 project, while Martin is involved in 2, meaning that John has the highest availability.
"""


def smartAssigning(names, statuses, projects, tasks):
    return [z for z in sorted(zip(tasks, projects, statuses, names)) if z[2] is False][0][3]

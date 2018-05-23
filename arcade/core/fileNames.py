"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

"""

			
def fileNaming(names):
    results = []
    for name in names:
        if name in results:
            counter = 1
            new_name = name
            while new_name in results:
                new_name = name + '(' + str(counter) + ')'
                counter += 1
            name = new_name
        results.append(name)
    return results

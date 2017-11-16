"""
Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.

Example

For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
swapLexOrder(str, pairs) = "dbca".

By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".
"""



def return_element(val, l):
    for i, el in enumerate(l):
        if val in el:
            return i
    return None

def get_connected_components(connections):
    components = []
    for i, conn in enumerate(connections):
        if i == 0:
            components.append([p for p in conn])
        else:
            exist = False
            for p in conn:
                ind = return_element(p, components)
                if ind is not None:
                    components[ind] += [x for x in conn if x not in components[ind]]
                    exist = True
            if not exist:
                components.append([p for p in conn])
    return components

def swapLexOrder(string, pairs):
    components = pairs
    while True:
        results = get_connected_components(components)
        if results == components:
            break
        else:
            components = results
    
    components_values = []
    for i, s in enumerate(components):
        components[i].sort()
        values = [string[i - 1] for i in s]
        values.sort(reverse=True)
        components_values.append(values)
    
    str_list = list(string)
    for j, s in enumerate(components):
        for k, i in enumerate(s):
            str_list[i - 1] = components_values[j][k]
    return ''.join(str_list)

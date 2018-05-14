"""
Define crossover operation over two equal-length strings A and B as follows:

the result of that operation is a string of the same length as the input strings
result[i] is either A[i] or B[i], chosen at random
Given array of strings inputArray and a string result, find for how many pairs of strings from inputArray the result of the crossover operation over them may be equal to result.

Note that (A, B) and (B, A) are the same pair. Also note that the pair cannot include the same element of the array twice (however, if there are two equal elements in the array, they can form a pair).

Example

For inputArray = ["abc", "aaa", "aba", "bab"] and result = "bbb", the output should be
stringsCrossover(inputArray, result) = 2.
"""


def stringsCrossover(inputArray, result):
    counter = 0
    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            is_cross = True
            for k in range(len(inputArray[i])):
                if inputArray[i][k] != result[k] and inputArray[j][k] != result[k]:
                    is_cross = False
                    break
        if is_cross:
            counter += 1
    return counter


#takes in a non-empty array and a target sum. if sum of any two numbers mathches target sum, function return those numbers in an array.
def twoNumberSum(array, targetSum):
    for e in range(len(array) - 1):
        x = e + 1
        for z in range(x, len(array)):
            if array[e] + array[z] == targetSum:
                return [array[e], array[z]]

    return []



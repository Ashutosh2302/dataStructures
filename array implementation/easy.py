#takes in a non-empty array and a target sum. if sum of any two numbers mathches target sum, function return those numbers in an array.
def twoNumberSum(array, targetSum):
    for e in range(len(array) - 1):
        x = e + 1
        for z in range(x, len(array)):
            if array[e] + array[z] == targetSum:
                return [array[e], array[z]]

    return []

#function determines whether the second array is a sub-sequence of the first one.
def isValidSubsequence(array, sequence):
    index = []
    if len(array) < len(sequence):
        return False
    for e in sequence:
        try:
            index.append(array.index(e))
            array[array.index(e)] = 'a'
        except:
            return False
    for e in range(len(index) - 1):
        if index[e] > index[e + 1]:
            return False

    return True

#this function takes a sorted array as an input and returns a new array of same length with squares of original integers also sorted in ascending order
def sortedSquaredArray(array):
    l = []
    for e in array:
        x = e * e
        if len(l) == 0:
            l.append(x)
        elif len(l) == 1:
            if l[0] >= x:
                l.insert(0, x)
            else:
                l.append(x)
        else:
            for index in range(len(l) - 1):
                if l[index] <= x and l[index + 1] >= x:
                    l.insert(index + 1, x)
                    break
            else:
                if l[len(l) - 1] <= x:
                    l.append(x)
                else:
                    l.insert(0, x)

    return l
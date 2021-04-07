# function to move all the instances of the given integer in the array to the end of array and return the arrat
# note: the function performs this in place i.e it mutates the input array
def moveElementToEnd(array, toMove):
    if not array:
        return []
    index = 0
    t = len(array) - 1
    while (t != index):
        if array[index] == toMove:
            element = array.pop(index)
            array.append(element)
            t -= 1
        else:
            index += 1
    return array


# function to find the pair of numbers (one from each array) whose absoulte sum is closest to zero and returns an array containings these 2 numbers
def smallestDifference(arrayOne, arrayTwo):
    differeneceFromZero = {}
    for first in arrayOne:
        for second in arrayTwo:
            difference = abs(first - second) if first > second else abs(second - first)
            differeneceFromZero[abs(0 - difference)] = [first, second]
    x = list(differeneceFromZero.keys())[0]
    for key, value in differeneceFromZero.items():
        if key <= x:
            result = key
            x = key
    return differeneceFromZero[result]

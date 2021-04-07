#function to move all the instances of the given integer in the array to the end of array and return the arrat
#note: the function performs this in place i.e it mutates the input array
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
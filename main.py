## Python3 code to linearly search x in array[].
# If x is present then return its location,
# otherwise return -1
import random


def search(array, n, x):
    # operations = 0
    for i in range(0, n):
        # operations += 1
        if array[i] == x:
            # print("linear ops: ", operations)
            return i
    # print("linear ", operations)
    return -1


# Python3 Program for recursive binary search.
# Returns index of x in array if present, else -1

def binarySearch(array, l, r, x):
    # operations = 0
    while l <= r:
        # operations += 1
        mid = l + (r-l) // 2
        # check if x is present at mid
        if array[mid] == x:
            # print("binary ops: ", operations)
            print("this is mid == x: ", mid)
            return mid
        # if x is greater, ignore left half
        elif array[mid] < x:
            l = mid + 1
        # if x is smaller, ignore right half
        else:
            r = mid - 1

        # if we reach here, then the element was not present
       # print("binary ops: ", operations)
        return -1

    print("x: ", x)
    print("Index: ", arr.index(x))

if __name__ == "__main__":

    # Driver Code
    # ref: https://moonbooks.org/Articles/How-to-create-a-list-of-random-integers-in-python-/
    arr = [random.randint(0, 199) for i in range(200)]

    x = 20
    n = len(arr)

    import timeit
    iter = 10
    ltime = timeit.timeit(lambda: search(arr, n, x), setup = "from __main__ import binarySearch",
                          number=iter)
    btime = timeit.timeit(lambda: binarySearch(arr, 0, len(arr)-1, x),  setup="from __main__ import binarySearch",
                          number=iter)

    print("Length of array: ", n)
    print("X is: ", x, " at index: ", arr.index(x))
    print("Linear search took: ", ltime)
    print("Binary search took: ", btime)


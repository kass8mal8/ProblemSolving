"""
For example, a social networking company may want to see the effect of
a new UI on page visit duration without taking the chance of alienating all its users if the rollout is
unsuccessful.
Implement an algorithm that takes as input an array of distinct elements and a size, and returns
a subset of the given size of the array elements. All subsets should be equally likely. Return the
result in input array itself.
"""
from random import randint


def offline_data(arr, k):
    for x in range(k):
        i = randint(x, len(arr) - 1)
        arr[x], arr[i] = arr[i], arr[x]

        if len(arr) > k:
            for y in range(len(arr) - k):
                del arr[-y]
    return arr


array = [3, 7, 5, 11, 9, 21, 43, 13]
print(offline_data(array, 7))

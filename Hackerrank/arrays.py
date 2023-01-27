def arrays(arr):
    L = []
    for x in range(len(arr)):
        for y in range(x, len(arr)):
            if abs(arr[x] - arr[y]) <= 1:
                L.append(x)
        break

    return len(L)


array = [1, 2, 2, 3, 2, 1]
print(arrays(array))

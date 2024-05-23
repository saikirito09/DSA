def largeElement(arr):
    max = arr[0]
    for i in range(len(arr)):
        if (max < arr[i]):
            max = arr[i]
    return max

if __name__ == "__main__":
    arr = [2,5,1,3,0]
    print(largeElement(arr))

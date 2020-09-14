import random
# Arrays can be easily rotated through splicing. Simply remove the first n elements and add them
# back to the end of the array.

def rotateArrayLeft(arr, n):
    print("Left",n)
    return arr[n:] + arr[:n]


def rotateArrayRight(arr, n):
    n = n * -1
    print("Right",abs(n))
    return arr[n:] + arr[:n]


arr = [i + 1 for i in range(10)]  # efficient way to add numbers to array
n = random.randint(1, 9)
print(rotateArrayLeft(arr, n))
print("\n")
print(rotateArrayRight(arr, n))

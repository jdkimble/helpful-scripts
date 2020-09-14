def uniqueWords(s, t):
    unique = []
    s = s.split()
    t = t.split()

    for i in range(len(s)):
        if s[i] not in t:
            unique.append(s[i])

    for i in range(len(t)):
        if t[i] not in s:
            unique.append(t[i])
    return unique


def numIntersect(arr1, arr2):
    intersect = []
    for i in arr2:
        if i in arr1 and i not in intersect:
            intersect.append(i)
    return intersect


s1 = "the tortoise beat the haire"
s2 = "the tortoise lost to the haire"
print(uniqueWords(s1, s2))
print("\n")
arr1 = [1,3,5,7,9]
arr2 = [2,4,6,8,5]
print(numIntersect(arr1, arr2))
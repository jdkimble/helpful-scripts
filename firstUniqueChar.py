# This script will find the first unique character and return its position and letter.
# Returns -1 if there are no unique chars.
def first_unique(s):
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i, s[i]
    return -1


string = 'alksjdflkjsdfalskdjfhlaskjdfladjslfaj'
print(first_unique(string))

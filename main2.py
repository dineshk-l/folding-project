import math
crease_array = list(map(str,input()))
# print(crease_array)

def opposite(s, i, j):
    for n in range(i-1, j - 1, -1):
        if s[n-1] == s[i+(i-n)-1]:
            return False
    return True


def find_min_fold(s):
    n = len(s) + 1
    fold = [n] * n
    fold[0] = 0
    fold[1] = 1
    for i in range(2,len(s)+1):
        new_min = fold[i-1] + 1
        for j in range(i-1,0,-1):
            if (i-j+i<n):
                if  opposite(s, i, j):
                    new_min = min(new_min, fold[j-1]+1)    
            fold[i] = new_min
    return fold



def find_min(l1):
    min_value = l1[-1]
    for i in range(0, len(l1)-1):
        min_value = min(min_value,l1[i]+find_min_fold(crease_array[i+1:][::-1])[-1])
    return min_value




fold1 = find_min_fold(crease_array)[1:]

#print(fold1)
#print(find_min_fold(crease_array[::-1])[1:][::-1])
#print(fold1[-1])

min_value = find_min(fold1)
print(min_value)
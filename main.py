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

def create_tuple(fold2):
    res = [0] * len(fold2)
    for i in range(1,len(fold2)):
        for j in range(i-1,-1,-1):
            if fold2[j]<fold2[i]:
                res[i] = max(res[j]-(i-j),0,res[i])
                break
            elif fold2[j] >= fold2[i]:
                res[i] += 1
            
    return list(zip(fold2,res))

def find_min(l1, l2):
    n = 0
    min_value = l1[-1]
    for i in range(n, len(l1)-2):
        r = l2[i+1][1]
        if r <= 0:
            min_value = min(min_value, l1[i]+l2[i+1][0])
    return min_value



fold2 = find_min_fold(crease_array[::-1])[1:]
fold1 = find_min_fold(crease_array)[1:]

# print(fold1)
# print(list(reversed(fold2)))
# print(fold1[-1])
s  = create_tuple(fold2)
s1 = create_tuple(fold1)
min_value = min(find_min(fold1, list(reversed(s))),find_min(fold2, list(reversed(s1))))
print(min_value)
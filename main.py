s = list(map(str,input()))

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
    for i in range(1,len(s)+1):
        new_min = fold[i-1] + 1
        for j in range(i,-1,-1):
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
    min_value = l1[-1]
    for i in range(0, len(l1)):
        for j in range(1,len(l1)-i):
            r = l2[i+j][1]
            if r == j-1:
                min_value = min(min_value, l1[i]+l2[i+j][0]+j-1)
    return min_value

def dragon(crease_array):
    fold2 = find_min_fold(crease_array[::-1])[1:]
    fold1 = find_min_fold(crease_array)[1:]
    l  =  list(reversed(create_tuple(fold2)))
    l1 = list(reversed(create_tuple(fold1)))
    min_value = min(find_min(fold1,l),find_min(fold2, l1))
    return min_value

print(dragon(s))
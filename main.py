crease_array = list(map(str,input()))
# print(crease_array)

def opposite(s, i, j):
    for n in range(i-1, j - 1, -1):
        if n-1 >= 0 and n-1 < len(s) and i+(i-n)-1 >= 0 and i+(i-n)-1 < len(s):
            if s[n-1] == s[i+(i-n)-1]:
                return False
    return True


def find_min_fold(s):
    n = len(s) 
    fold = [n] * n
    fold[0] = 0
    fold[1] = 1
    for i in range(2,len(s)):
        new_min = fold[i-1] + 1
        for j in range(i-1,0,-1):
            if (i-j >= n - i):
                if  opposite(s, i, j):
                    new_min = min(new_min, fold[j-1]+1)    
            fold[i] = new_min
    return fold[-1]

print(find_min_fold(crease_array))
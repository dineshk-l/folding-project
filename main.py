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

def find_optimal_fold(fold1, fold2):
    min_sum = min(fold1[-1],fold2[0])
    for i in range(int(len(fold1)/2),len(fold1)-1):
        min_sum = min(min_sum, fold1[i]+fold2[i+1])
    print(min_sum)


fold1 = find_min_fold(crease_array)[1:]
print(fold1)
fold2 = find_min_fold(crease_array[::-1])[::-1][:-1]
print(fold2)
print(find_optimal_fold(fold1, fold2))
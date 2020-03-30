inversions = 0
def merge_and_count_inversions(left , right):
    global inversions
    i=0
    j=0
    result = []
    inversions_indicies = []
    while i < len(left) and j <len(right):
        if right[j]<left[i]:
            result.append(right[j])
            j +=1
            if j  not in inversions_indicies:
                inversions_indicies.append(j)
                inversions += len(left) - i  
        else:
            result.append(left[i])
            i += 1
    while i <len(left):
        result.append(left[i])
        i += 1
        if j  not in inversions_indicies:
                inversions_indicies.append(j)
                inversions += len(left) - i  
    while j <len(right):
        result.append(right[j])
        j += 1
    return result
    
def merge_sort_and_count_inversions(ints_list):
    if len(ints_list) < 2:
        return ints_list[:]
    else:
        middle =len(ints_list)//2
        left = merge_sort_and_count_inversions(ints_list[:middle])
        right= merge_sort_and_count_inversions(ints_list[middle:])
        return merge_and_count_inversions(left,right)
    
ints = open('IntegerArray.txt','r')
ints_list = list(map(int,ints.read().split('\n')[:-1]))
ints.close()

print(merge_sort_and_count_inversions(ints_list))
print(inversions)

import random

# Merge Sort
def merge(left, right):
    result = []
    i, j = 0, 0
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
      
    while(i< len(left)):
        result.append(left[i])
        i+=1
    
    while(j< len(right)):
        result.append(right[j])
        j+=1
   
    return result

def merge_sort(L):
    if(len(L) < 2):
        return L
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def run_merge_sort():
    L = [random.randint(0, 100) for i in range(10)]
    print(merge_sort(L))


# Insertion Sort

def insertion_sort(L):
    for i in range(1, len(L)):
        j = i
        while L[j-1] > L[j] and j > 0:
            L[j-1], L[j] = L[j], L[j-1]
            j-=1
    return L

def run_insertion_sort():
    L = [random.randint(0, 100) for i in range(10)]
    print(insertion_sort(L))


# Selection Sort

def selection_sort(L):
    index = 0
    while index != len(L):
        for i in range(index, len(L)):
            if(L[i] < L[index]):
                L[index],L[i] = L[i],L[index]
        index+=1
    return L

def run_selection_sort():
    L = [random.randint(0, 100) for i in range(10)]
    print(selection_sort(L))


# Quick Sort

def quick_sort(L):
    if(len(L) < 2):
        return L

    greater = []
    less = []
    pivot = L.pop()

    for i in L:
        if i > pivot:
            greater.append(i)
        else:
            less.append(i)
    
    return quick_sort(less) + [pivot] + quick_sort(greater)

def run_quick_sort():
    L = [random.randint(0, 100) for i in range(10)]
    print(quick_sort(L))

run_quick_sort()
def get_permutations(sequence):
    if(len(sequence) <= 1): 
        return sequence
    
    sub_permutations = get_permutations(sequence[1:])

    permutation_list = []
    for permutation in sub_permutations:
        for i in range(len(permutation) + 1): 
            new_permutation = permutation[:i] + sequence[0] + permutation[i:]
            permutation_list.append(new_permutation)
    
    return permutation_list

print(get_permutations("abc"))
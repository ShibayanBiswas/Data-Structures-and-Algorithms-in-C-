'''

The basic idea is to generate all the possible permutations of ‘N’ integers and find the lexicographically next greater permutation.
1. Generate all the possible permutations of ‘N’ integers.
2. Store all the permutations in a 2D array/list.
3. Sort the list of permutations in lexicographically ascending order.
4. Find the index of the input permutation in the sorted list. Let say the index is ‘i’.
        * If the given permutation is present at the end of the array/list, no other greater permutation can exist, so print the smallest permutation.
        * Otherwise, return the permutation which is present at the (i+1)th index in the list.

Time Complexity : O((N * N!) * log(N * N!)), where ‘N!’ is the factorial of the length of the given permutation. Since we are 
generating and storing all possible permutations of ‘N’ length and then sorting them in lexicographical order. Thus, the overall 
time complexity will be O((N * N!) * log(N * N!)).

Space Complexity : O(N * N!), where ‘N’ is the length of the given permutation. Since we are storing all possible permutations of 
‘N’ length. Thus, the overall space complexity will be O(N * N!).

'''

import functools

def compare(lista, listb):
    
    for i in range(len(lista)):

        if lista[i] == listb[i]:
            # Move to next element.
            continue

        return lista[i] - listb[i]

    return 0

# Generates all the permutations and store it in the vector.
def getAllPermutations(p, l, r, permutations):
    # Base case.
    if l == r:
        # Store the new permutation in a new container as directly storing the old container 'p' would cause problems.
        temp = list(p)
        permutations.append(temp)

    else:
        # Make new permutations.
        for i in range(l, r + 1):
            # Swapping.
            p[l], p[i] = p[i], p[l]

            getAllPermutations(p, l + 1, r, permutations)
            # Backtrack.
            p[l], p[i] = p[i], p[l]

    return

def nextPermutation(permutation, n):

    # To store all the permutations.
    permutations = []

    getAllPermutations(permutation, 0, n - 1, permutations)
    # Sort the list of permutations lexicographically.
    permutations.sort(key=functools.cmp_to_key(compare))
    # Iterate to find the index of the given permutaion 'p'.
    for i in range(len(permutations)):

        if permutations[i] == permutation:
            # Index of the given permutation found.
            if i != len(permutations) - 1:
                # Return the next greater one.
                return permutations[i + 1]

            
    # Next permutation not possible.
    return permutations[0]

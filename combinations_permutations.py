# create a list that contains all the English alphabet
# create a list that contains all the numbers from 0 to 9
# create a list that contains all the special characters
# permute and combine the three lists above 

# permute
def permute(list1, list2, list3):
    # create a list that will contain all the permutations
    permutations = []
    # iterate through the first list
    for i in list1:
        # iterate through the second list
        for j in list2:
            # iterate through the third list
            for k in list3:
                # create a string that contains the current permutation
                permutation = i + j + k
                # add the permutation to the list of permutations
                permutations.append(permutation)
    # return the list of permutations
    return permutations


print("List of permutations")
print(permute(["a", "b", "c"], ["1", "2", "3"], ["!", "@", "#"]))

##################################################################
# combination
def combination(list1, list2, list3):
    # create a list that will contain all the combinations
    combinations = []
    # iterate through the first list
    for i in list1:
        # iterate through the second list
        for j in list2:
            # iterate through the third list
            for k in list3:
                # create a string that contains the current combination
                combination = [[i+j+k], [i+k+j], [j+i+k], [j+k+i], [k+i+j], [k+j+i]]
                # add the combination to the list of combinations
                combinations.append(combination)
    # return the list of combinations
    return combinations
print("List of combinations")    
print(combination(["a", "b", "c"], ["1", "2", "3"], ["!", "@", "#"]))

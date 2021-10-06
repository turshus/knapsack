"""
Created by: Connor Meads
A01853906
 Flow of Program:
 SINGLE KNAPSACK PROBLEM:
    recursive solution
    Memoizing Solution
    DP Solution

 DOUBLE KNAPSACK PROBLEM:
    recursive solution
    Memoizing Solution
    DP Solution
"""

import random

#Global variabes
g_objects = []
g_memoizingSolution = {}

g_sizes = []
g_values = []

#Horribly long algorithm to find the optimal knapsack size
def canFillKnapSackRecursively(a_knapsackSize, a_numObjects):
    if a_knapsackSize < 0:
        return False
    elif a_knapsackSize == 0:
        return True
    if a_numObjects == 0:
        return False
    
    return (canFillKnapSackRecursively(a_knapsackSize - g_objects[a_numObjects - 1], a_numObjects - 1) 
           or canFillKnapSackRecursively(a_knapsackSize, a_numObjects - 1))

def canFillKnapsackMemoizing(a_knapsackSize, a_numObjects):
    if a_knapsackSize < 0:
        return False
    elif a_knapsackSize == 0:
        return True
    if a_numObjects == 0:
        return False
    
    #if we already have that solution in memory, return it
    if (a_knapsackSize, a_numObjects) in g_memoizingSolution:
        return g_memoizingSolution[(a_knapsackSize, a_numObjects)]
    
    #if we don't have it in memory, solve for it
    g_memoizingSolution[(a_knapsackSize, a_numObjects)] = canFillKnapsackMemoizing(a_knapsackSize - g_objects[a_numObjects - 1], a_numObjects - 1) or canFillKnapsackMemoizing(a_knapsackSize, a_numObjects - 1)
    return g_memoizingSolution[(a_knapsackSize, a_numObjects)]

def canFillKnapsackDP(a_knapsackSize, a_numObjects):
    l_dpSolutions = {}

    #for every object, if the knapsack size is 0, it is always true
    for i in range(0, a_numObjects + 1):
        l_dpSolutions[(i, 0)] = True
    
    #for every knapsack size, if the number of objects is 0, it is always false
    for j in range(0, a_knapsackSize + 1):
        l_dpSolutions[(0, j)] = False

    for i in range(1, a_numObjects + 1):
        for j in range(1, a_knapsackSize + 1):
            newSize = j - g_objects[i - 1]
            if newSize < 0:
                l_dpSolutions[(i, j)] = l_dpSolutions[(j, i - 1)]
            else:  
                l_dpSolutions[(i, j)] = (l_dpSolutions[(j - g_objects[i - 1], i - 1)] 
                or l_dpSolutions[(j, i - 1)])
    return l_dpSolutions[(a_knapsackSize, a_numObjects)]

#DOUBLE KNAPSACK PROBLEM
def maxValueInKnapsacksRecursive(a_knapsackOneSize, a_knapsackTwoSize, a_numObjects):
    #Simple Problem, Simple Solution
    #checks the size of the sizes array.  If it's empty, we have nothing to put in our knapsack, so we return 0.0 as our value
    if a_numObjects == 0:
        return 0.0
    #checks if both the knapsacks have any room left in them.  If they don't, return 0.0 
    if a_knapsackOneSize == 0 and a_knapsackTwoSize == 0:
        return 0.0
    
    #Recurse down until the size of the knapsacks is either 0 or cannot contain anymore objects
    
    

    

def maxValueInKnapsacksMemoizing(a_knapsackOneSize, a_knapsackTwoSize):
    return 0.0

def maxValueInKnapsacksDP(a_knapsackOneSize, a_knapsackTwoSize):
    return 0.0

if __name__ == "__main__":
    print("Starting Program")

    #Create a knapsack of a random size
    l_knapsackOneSize = random.randint(0, 100)
    print("1st Knapsack Size: ", l_knapsackOneSize)

    l_knapsackTwoSize = random.randint(0, 100)
    print(f"2nd Knapsack Size: {l_knapsackTwoSize}")

    # #Fill the g_objects array full of random numbers
    # for i in range(l_knapsackOneSize):
    #     g_objects.append(random.randint(1, 3))
    # print(f'Knapsack contents: {g_objects}')

    # # #Recursive Algorithm Call
    # # print('\nRecursive Call')
    # # print(canFillKnapSackRecursively(l_knapsackOneSize, len(g_objects)))

    # # #Dynamic Programming call
    # # print('\nMemoizing Call')
    # # print(canFillKnapsackMemoizing(l_knapsackOneSize, len(g_objects)))

    #Fill the g_sizes and g_values with objects
    l_numObj = random.randint(0, 2000)
    for i in range(0, l_numObj):
        g_sizes.append(random.randint(1, 1000))
        g_values.append(round(random.uniform(1.0, 1200), 2))

    print('\nRecursive call to max value')
    print(maxValueInKnapsacksRecursive(l_knapsackOneSize, l_knapsackTwoSize, l_numObj))

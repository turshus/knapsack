import random
from time import time

#global variables
sizes = []
values = []

memoizingCache = []

def maxValueRecursive(k1, k2, numObj):
    if k1 == 0 and k2 == 0:
        return 0.0
    if numObj == 0:
        return 0.0

    value1 = 0.0 #Knapsack 1 value
    value2 = 0.0 #knapsack 2 value
    value3 = 0.0 #knapsack 3 value
    if k1 - sizes[numObj] >= 0:
        value1 = maxValueRecursive(k1 - sizes[numObj], k2, numObj - 1) + values[numObj]
    if k2 - sizes[numObj] >= 0:
        value2 = maxValueRecursive(k1, k2 - sizes[numObj], numObj - 1) + values[numObj]
    value3 = maxValueRecursive(k1, k2, numObj - 1)
    
    return max(value1, value2, value3)

def maxValueMemoizing(k1, k2, numObj):
    if k1 == 0 and k2 == 0:
        return 0.0
    if numObj == 0:
        return 0.0
    
    #check if solution as already been solved
    if(k1, k2, numObj) in memoizingCache:
        return memoizingCache[k2][k1][numObj]
    
    value1 = 0.0
    value2 = 0.0
    value3 = 0.0
    if k1 - sizes[numObj] >= 0:
        value1 = maxValueMemoizing(k1 - sizes[numObj], k2, numObj - 1) + values[numObj]
    if k2 - sizes[numObj] >= 0:
        value2 = maxValueMemoizing(k1, k2 - sizes[numObj], numObj - 1) + values[numObj]
    value3 = maxValueMemoizing(k1, k2, numObj - 1)

    memoizingCache[k2][k1][numObj] = max(value1, value2, value3)

    return memoizingCache[k2][k1][numObj]

def maxValueDP(k1, k2, totNumObj):
    dpCache = [[[-1.0 for j in range(totNumObj + 1)] for k in range(k1 + 1)] for z in range(k2 + 1)]
    #[k2][k1][totNumObj]
    #Base case
    for currNumObj in range(totNumObj):
        dpCache[0][0][currNumObj] = 0.0

    for i in range(k1 + 1):
        for j in range(k2 + 1):
            dpCache[j][i][0] = 0.0

    for currNumObj in range(1, totNumObj + 1):
        for k2Spaces in range(0, k2 + 1):
            for k1Space in range(0, k1 + 1):
                value1 = 0.0
                value2 = 0.0
                value3 = 0.0
                if not (k2Spaces == 0 and k1Space == 0):
                    if k1Space - sizes[currNumObj] >= 0:
                        value1 = values[currNumObj] + dpCache[k2Spaces][k1Space - sizes[currNumObj]][currNumObj - 1]
                    if k2Spaces - sizes[currNumObj] >= 0:
                        value2 = values[currNumObj] + dpCache[k2Spaces - sizes[currNumObj]][k1Space][currNumObj - 1]
                    value3 = dpCache[k2Spaces][k1Space][totNumObj - 1]

                    dpCache[k2Spaces][k1Space][currNumObj] = max(value1, value2, value3)

    return dpCache[k2][k1][totNumObj - 1]

def problemGen(a_arraySize, a_aveSize):
    l_items = [] #This value holds the sizes[] array at index 0 and values[] array at index 1
    l_sizes = []
    l_values = [] 
    for i in range(0, a_arraySize):
        #generate sizes
        l_sizes.append(random.randint(1, 2 * a_aveSize))
        l_values.append(round(random.uniform(1.0, i + random.randint(1, 50)), 2))
        
    l_items.append(l_sizes)
    l_items.append(l_values)
    return l_items

if __name__ == "__main__":
    # print('Starting Program')

    # print('\nStarting Recursion...')
    # numRecursiveCalls = 30
    # startRecursion = time()
    # #Recursive Calls to find solution to knapsack problem
    # for i in range(0, numRecursiveCalls):
    #     l_items = problemGen(i, i)
    #     sizes = l_items[0]
    #     values = l_items[1]

    #     print(f'\n\nROUND {i}\nk1: {i}\nk2: {i}\nsizes: {l_items[0]}\nvalues: {l_items[1]}')

    #     startCall = time()
    #     print(f"Value: {maxValueRecursive(i, i, len(l_items[0]))} calculated in {(time() - startCall):.4f} seconds")
    # print(f'\n\nEnding Recursion\nTotal Recursive time to run through {numRecursiveCalls} calls: {(time() - startRecursion):.4f}\n\n')

    # print('Starting Memoizing...')
    # knapsackSize = 30
    # startMemoizing = time()

    # for i in range(0, knapsackSize):
    #     l_items = problemGen(i, i)
    #     sizes = l_items[0]
    #     values = l_items[1]

    #     #Clear the cache for the new round
    #     memoizingCache = [[[-1 for j in range(len(l_items[0]) + 1)] for k in range(i + 1)] for z in range(i + 1)]

    #     print(f'\n\nROUND {i}\nk1: {i}\nk2: {i}\nsizes: {l_items[0]}\nvalues: {l_items[1]}')

    #     startCall = time()
    #     print(f'Value: {maxValueMemoizing(i, i, len(l_items[0]))} calculated in {(time() - startCall):.4f} seconds')    
    # print(f'\n\nEnding Memoizing\nTotal Memoizing time to run through {knapsackSize} calls: {(time() - startMemoizing):.4f} seconds\n\n')

    # print('Starting DP...')
    # numDPCalls = 30
    # startDP = time()

    # for i in range(0, numDPCalls):
    #     l_items = problemGen(i, i)
    #     sizes = l_items[0]
    #     values = l_items[1]

    #     print(f'\n\nROUND {i}\nk1: {i}\nk2: {i}\nsizes: {l_items[0]}\nvalues: {l_items[1]}')

    #     startCall = time()
    #     print(f'Value: {maxValueDP(len(l_items[0]), i, i)} calculated in {(time() - startCall):.4f} seconds')    
    # print(f'\n\nEnding DP\nTotal DP time to run through {numDPCalls} calls: {(time() - startDP):.4f} seconds\n\n')



    #Simple, predictable problem
    sizes = [None, 3, 2, 3, 2, 1, 5]
    values = [None, 2, 3, 5, 3, 6, 3]
    k1 = 7
    k2 = 4

    memoizingCache = [[[-1 for j in range(len(sizes) + 1)] for k in range(k1 + 1)] for z in range(k2 + 1)]

    print(f"Recursive: {maxValueRecursive(k1, k2, len(sizes) - 1)}")
    print(f"Memoizing: {maxValueMemoizing(k1, k2, len(sizes) - 1)}")
    print(f"DP: {maxValueDP(k1, k2, len(sizes) - 1)}")

    print('\n##########################################\n            Finished Program')
    print('##########################################')
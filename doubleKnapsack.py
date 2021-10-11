import random
from time import time

#global variables
sizes = []
values = []

memoizingCache = []

def maxValueRecursive(k1, k2, sizeOfArray):
    if k1 == 0 and k2 == 0:
        return 0.0
    if sizeOfArray-1 < 0:
        return 0.0

    value1 = 0.0
    value2 = 0.0
    value3 = 0.0
    if k1 - sizes[sizeOfArray - 1] >= 0:
        value1 = maxValueRecursive(k1 - sizes[sizeOfArray - 1], k2, sizeOfArray - 1) + values[sizeOfArray - 1]
    if k2 - sizes[sizeOfArray - 1] >= 0:
        value2 = maxValueRecursive(k1, k2 - sizes[sizeOfArray - 1], sizeOfArray - 1) + values[sizeOfArray - 1]
    value3 = maxValueRecursive(k1, k2, sizeOfArray - 1)
    
    return max(value1, value2, value3)

def maxValueMemoizing(k1, k2, i):
    if k1 == 0 and k2 == 0:
        return 0.0
    if i-1 < 0:
        return 0.0

    #Check if solution has already been solved, return it
    if (k1, k2, i) in memoizingCache:
        return memoizingCache[k1][k2][i]
    
    value1 = 0
    value2 = 0
    value3 = 0
    if k1 - sizes[i - 1] >= 0:
        value1 = maxValueMemoizing(k1 - sizes[i - 1], k2, i - 1) + values[i - 1]
    if k2 - sizes[i - 1] >= 0:
        value2 = maxValueMemoizing(k1, k2 - sizes[i - 1], i - 1) + values[i - 1]
    value3 = maxValueMemoizing(k1, k2, i - 1)

    memoizingCache[k1][k2][i] = max(value1, value2, value3)
    
    return memoizingCache[k1][k2][i]

def maxValueDP(k1, k2, sizeOfArray):
    dpCache = [[[-1.0 for j in range(sizeOfArray + 1)] for k in range(k1 + 1)] for z in range(k2 + 1)]

    for i in range(sizeOfArray):
        dpCache[0][0][i] = 0.0

    for i in range(sizeOfArray):
        for k1Space in range(k1):
            for k2Space in range(k2):
                value1 = 0.0
                value2 = 0.0
                value3 = 0.0

                if k1Space - sizes[i] >= 0:
                    value1 = values[i] + dpCache[i - 1][k1Space - sizes[i]][k2Space]
                if k2Space - sizes[i] >= 0:
                    

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
    print('Starting Program')

    print('\nStarting Recursion...')
    numRecursiveCalls = 30
    startRecursion = time()
    #Recursive Calls to find solution to knapsack problem
    for i in range(0, numRecursiveCalls):
        l_items = problemGen(i, i)
        sizes = l_items[0]
        values = l_items[1]

        print(f'\n\nROUND {i}\nk1: {i}\nk2: {i}\nsizes: {l_items[0]}\nvalues: {l_items[1]}')

        startCall = time()
        print(f"Value: {maxValueRecursive(i, i, len(l_items[0]))} calculated in {(time() - startCall):.4f} seconds")
    print(f'\n\nEnding Recursion\nTotal Recursive time to run through {numRecursiveCalls} calls: {(time() - startRecursion):.4f}\n\n')

    print('Starting Memoizing...')
    numMemoizingCalls = 30
    startMemoizing = time()

    for i in range(0, numMemoizingCalls):
        l_items = problemGen(i, i)
        sizes = l_items[0]
        values = l_items[1]

        #Clear the cache for the new round
        memoizingCache = [[[-1 for j in range(len(l_items[0]) + 1)] for k in range(i + 1)] for z in range(i + 1)]

        print(f'\n\nROUND {i}\nk1: {i}\nk2: {i}\nsizes: {l_items[0]}\nvalues: {l_items[1]}')

        startCall = time()
        print(f'Value: {maxValueMemoizing(i, i, len(l_items[0]))} calculated in {(time() - startCall):.4f} seconds')    
    print(f'\n\nEnding Memoizing\nTotal Memoizing time to run through {numMemoizingCalls} calls: {(time() - startMemoizing):.4f} seconds\n\n')

    print('Starting DP...')
    numDPCalls = 30
    startDP = time()

    for i in range(0, numDPCalls):
        l_items = problemGen(i, i)
        sizes = l_items[0]
        values = l_items[1]

        print(f'\n\nROUND {i}\nk1: {i}\nk2: {i}\nsizes: {l_items[0]}\nvalues: {l_items[1]}')

        startCall = time()
        print(f'Value: {maxValueDP(i, i, len(l_items[0]))} calculated in {(time() - startCall):.4f} seconds')    
    print(f'\n\nEnding DP\nTotal DP time to run through {numDPCalls} calls: {(time() - startDP):.4f} seconds\n\n')


    print('\n##########################################\n            Finished Program')
    print('##########################################')
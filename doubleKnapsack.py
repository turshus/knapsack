import random
from time import time

#global variables
sizes = []
values = []

def maxValueRecursive(k1, k2, i):
    if k1 == 0 and k2 == 0:
        return 0.0
    if i-1 < 0:
        return 0.0

    value1 = 0.0
    value2 = 0.0
    value3 = 0.0
    if k1 - sizes[i - 1] >= 0:
        value1 = maxValueRecursive(k1 - sizes[i - 1], k2, i - 1) + values[i - 1]
    if k2 - sizes[i - 1] >= 0:
        value2 = maxValueRecursive(k1, k2 - sizes[i - 1], i - 1) + values[i - 1]
    value3 = maxValueRecursive(k1, k2, i - 1)
    
    return max(value1, value2, value3)

def problemGen(a_arraySize, a_aveSize):
    l_items = [] #This value holds the sizes[] array at index 0 and values[] array at index 1
    l_sizes = []
    l_values = [] 
    for i in range(0, a_arraySize):
        #generate sizes
        #l_sizes.append(random.randint(1, 2 * a_aveSize))
        l_sizes.append(random.randint(1, 5))
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
    print(f'\n\nEnding Recursion\nTotal Recursive time to run through {numRecursiveCalls} calls: {time() - startRecursion}\n\n')

    

    print('Finished Program')















    #Custom Problem Generator
    '''
    #Create progressively larger and larger knapsacks and lists
    for i in range(0, 30):
        l_k1Size = i + random.randint(0, 3)
        l_k2Size = i + random.randint(0, 3)

        l_sizes = []
        l_values = []

        #fill out the sizes and values
        for j in range(0, i + random.randint(0, 3)):
            l_sizes.append(j + random.randint(1, 4))
            l_values.append(j + round(random.uniform(0.0, i + 5.0), 2))
        
        
        print(f'\n\nROUND {i}\nk1: {l_k1Size}\nk2: {l_k2Size}\nsizes:  ({len(l_sizes)}) | {l_sizes}\nvalues: ({len(l_sizes)}) | {l_values}')
        start = time()
        print(f'$$Max Value$$ : {knapsacksValue(l_k1Size, l_k2Size, l_sizes, l_values)} in {(time() - start):.4f} seconds')

    #Create random knapsack sizes and random values & sizes arrays
   # l_k1Size = random.randint(1, 10)
    #l_k2Size = random.randint(1, 10)
    #l_sizes = []
    #l_values = []

    #for i in range(1, random.randint(2, 25)):
    #    l_sizes.append(i + random.randint(0, 4))
    #    l_values.append(i + round(random.uniform(0.0, 10.0), 2))

    #print(f'\n\nROUND {i}\nk1: {l_k1Size}\nk2: {l_k2Size}\nsizes: ({len(l_sizes)}) | {l_sizes}\nvalues: ({len(l_sizes)}) | {l_values}')
    #print(f'$$Max Value$$ : {knapsacksValue(l_k1Size, l_k2Size, l_sizes, l_values)}')


    #Custom Cases
    l_k1Size = 1
    l_k2Size = 3
    l_sizes = [1, 2, 3]
    l_values = [10, 15, 30]
    
    #print(f'l_k1Size: {l_k1Size}\nl_k2Size: {l_k2Size}\nsizes: {len(l_sizes)}\nvalues: {len(l_values)}')
    #print(knapsacksValue(l_k1Size, l_k2Size, l_sizes, l_values))
    '''
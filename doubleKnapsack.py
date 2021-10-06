import random
from time import time

def knapsacksValue(a_k1Size, a_k2Size, a_sizes, a_values):
    if a_k1Size == 0 and a_k2Size == 0:
        return 0.0
    if len(a_sizes) == 0:
        return 0.0

    highestValue = 0
    for i in range(0, len(a_sizes)):
        if a_k1Size >= a_sizes[i]:
            value = knapsacksValue(a_k1Size - a_sizes[i], a_k2Size, a_sizes, a_values) + a_values[i]

            if value > highestValue:
                highestValue = value
        elif a_k2Size >= a_sizes[i]:
            value = knapsacksValue(a_k1Size, a_k2Size - a_sizes[i], a_sizes, a_values) + a_values[i]

            if value > highestValue:
                highestValue = value
    return highestValue

def problemGen(a_arraySize, a_aveSize):
    l_items = [] #This value holds the sizes[] array at index 0 and values[] array at index 1
    l_sizes = []
    l_values = [] 
    for i in range(0, arraySize):
        #generate sizes
        l_sizes.append(random.randint(1, 2 * a_aveSize))
        l_values.append(round(random.uniform(1.0, i + random.randint(1, 50))), 2)
        
    l_items.append(l_sizes)
    l_items.append(l_values)
    return l_items

if __name__ == "__main__":
    print('Starting Program')
    
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


    '''#Custom Cases
    l_k1Size = 1
    l_k2Size = 3
    l_sizes = [1, 2, 3]
    l_values = [10, 15, 30]
    '''
    #print(f'l_k1Size: {l_k1Size}\nl_k2Size: {l_k2Size}\nsizes: {len(l_sizes)}\nvalues: {len(l_values)}')
    #print(knapsacksValue(l_k1Size, l_k2Size, l_sizes, l_values))

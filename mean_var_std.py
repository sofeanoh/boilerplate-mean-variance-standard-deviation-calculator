import numpy as np

def calculate(list):


        # Ensure the list contains exactly nine elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    #convert list into numpy array 3x3
    numpyArray = np.array(list)
    my_3x3_array = numpyArray.reshape(3,3)

    calculations = {
        'mean': calMean(my_3x3_array),
        'variance': calVariance(my_3x3_array),
        'standard deviation': calStd(my_3x3_array),
        'max': calMax(my_3x3_array),
        'min': calMin(my_3x3_array),
        'sum': calSum(my_3x3_array)
    }

    return calculations

def calMean(the_3x3array):

    axis0 = the_3x3array.mean(axis=0).tolist()
    axis1 = the_3x3array.mean(axis=1).tolist()
    flatten = the_3x3array.mean().tolist()

    return [axis0, axis1, flatten]

def calVariance(the_3x3array):

    axis0 = the_3x3array.var(axis=0).tolist()
    axis1 = the_3x3array.var(axis=1).tolist()
    flatten = the_3x3array.var().tolist()

    return [axis0, axis1, flatten]

def calStd(the_3x3array):

    axis0 = the_3x3array.std(axis=0).tolist()
    axis1 = the_3x3array.std(axis=1).tolist()
    flatten = the_3x3array.std().tolist()

    return [axis0, axis1, flatten]

def calMax(the_3x3array):

    axis0 = the_3x3array.max(axis=0).tolist()
    axis1 = the_3x3array.max(axis=1).tolist()
    flatten = the_3x3array.max().tolist()

    return [axis0, axis1, flatten]

def calMin(the_3x3array):

    axis0 = the_3x3array.min(axis=0).tolist()
    axis1 = the_3x3array.min(axis=1).tolist()
    flatten = the_3x3array.min().tolist()

    return [axis0, axis1, flatten]

def calSum(the_3x3array):

    axis0 = the_3x3array.sum(axis=0).tolist()
    axis1 = the_3x3array.sum(axis=1).tolist()
    flatten = the_3x3array.sum().tolist()

    return [axis0, axis1, flatten]


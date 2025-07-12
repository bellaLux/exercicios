import numpy as np
def calculate(num_list):
    if len(num_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(num_list)
    matrix.resize(3, 3)
    
    results = {"mean" : [],
               "variance" : [],
               "standard deviation" : [],
               "max" : [],
               "min" : [],
               "sum" : []
               }
    

    results["mean"].append([item for item in matrix.mean(axis=0)])
    results["mean"].append([item for item in matrix.mean(axis=1)])
    results["mean"].append(matrix.mean())

    results["variance"].append([item for item in matrix.var(axis=0)])
    results["variance"].append([item for item in matrix.var(axis=1)])
    results["variance"].append(matrix.var())

    results["standard deviation"].append([item for item in matrix.std(axis=0)])
    results["standard deviation"].append([item for item in matrix.std(axis=1)])
    results["standard deviation"].append(matrix.std())

    results["max"].append([item for item in matrix.max(axis=0)])
    results["max"].append([item for item in matrix.max(axis=1)])
    results["max"].append(matrix.max())

    results["min"].append([item for item in matrix.min(axis=0)])
    results["min"].append([item for item in matrix.min(axis=1)])
    results["min"].append(matrix.min())

    results["sum"].append([item for item in matrix.sum(axis=0)])
    results["sum"].append([item for item in matrix.sum(axis=1)])
    results["sum"].append(matrix.sum())


    return results

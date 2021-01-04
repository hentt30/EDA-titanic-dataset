"""
Trimmed mean function
"""
from math import sqrt

def _score_at_percentile(values:list,percent:float)->int:
    """
    Return a index in which the values
    perpassed thar percentile
    """
    total_size = len(values)
    for index,_ in enumerate(values):
        if (index+1)*100.0/total_size >= percent:
            return index
def _mean(values:list)->float:
    """
    Return mean
    """
    return sum(values)*1.0/len(values)

def _std(values:list)->float:
    """
    Return standar deviation
    """
    mean = _mean(values)
    size = len(values)
    squared_deviations = [(x-mean)**2 for x in values]

    return sqrt(sum(squared_deviations)*1.0/(size-1))
    

def trimmed_mean(values:list,percent:float)->float:
    """
    Get a list of values and return a trimmed
    mean
    """
    cleanedList = sorted([x for x in values if str(x) != 'nan'])
    lower_limit = _score_at_percentile(cleanedList, percent)
    upper_limit = _score_at_percentile(cleanedList, 100-percent)
    trimmed_list = cleanedList[lower_limit:upper_limit]
    return _mean(trimmed_list)


def trimmed_std(values:list,percent:float)->float:
    """
    Get a list of values and return a trimmed
    mean
    """
    cleanedList = sorted([x for x in values if str(x) != 'nan'])
    lower_limit = _score_at_percentile(cleanedList, percent)
    upper_limit = _score_at_percentile(cleanedList, 100-percent)
    trimmed_list = cleanedList[lower_limit:upper_limit]
    return _std(trimmed_list)


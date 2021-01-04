"""
Implements mad
"""

def _median(values:list):
    """
    Returns median
    """
    values = sorted(values)
    if len(values)%2 == 0:
        index = int(len(values)/2)
        return (values[index-1] +values[index])*1.0/2
    index = int(len(values)/2)
    return values[index]


def mad(values:list):
    """
    Implements median absolute deviation
    """
    values = [x for x in values if str(x) != 'nan']
    median = _median(values)
    median_absolute_deviation = [abs(x-median) for x in values]
    mad = _median(median_absolute_deviation)
    return mad

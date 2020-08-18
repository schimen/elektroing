""" python functions for ISTT1002"""

import math

def average(numbers):
    """gjennomsnitt"""
    return sum(numbers)/len(numbers)

def median(numbers):
    """median"""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid_values = (sorted_numbers[n//2], sorted_numbers[n//2 + 1])
        return average(mid_values)
    
    else:
        return sorted_numbers[n//2]

def range(numbers):
    """variasjonsbredde"""
    return max(numbers) - min(numbers)

def sample_variance(numbers):
    """utvalgsvarianse/empirisk varians"""
    n = len(numbers)
    avg = average(numbers)
    return (1/(n-1))*sum([(number-avg)**2 for number in numbers])

def sample_standard_deviation(numbers):
    """utvalgsstandardavvik/empirisk standardavvik"""
    return math.sqrt(sample_variance(numbers))

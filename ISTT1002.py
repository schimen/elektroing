""" funksjoner for ISTT1002"""

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

def range_width(numbers):
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

def independent_union(p_union, *args):
    """
    tar først P(A_1∩A_2∩…∩A_n) og deretter P(A_1 ), P(A_2 ), …, P(A_n).
    funksjonen sjekker om disse er uavhengige
    """
    if p_union == math.prod(args):
        return True

    else:
        return False

def complement(p):
    """komplementærhendelse av sannsynlighet (desimal)"""
    return 1 - p

def addition_rule(*args, p=0):
    """addisjonsregelen (p = 0 så lenge data er disjunkt)"""
    return sum(args) - p

def expected_value_discrete(values, probabilities):
    """
    forventningsverdi for diskret stokastisk variabel
    tar først de diskrete verdienen og deretter deres sannsynligheter
    """ 
    cumulative_sum = 0
    for i in range(len(values)):
        cumulative_sum += values[i]*probabilities[i]

    return cumulative_sum

def variance_discrete(values, probabilities):
    """
    varians for diskrete stokatiske variabler
    tar først verdier og deretter tilhørende sannsynligheter
    """
    mu = expected_value_discrete(values, probabilities)
    new_values = [(value - mu)**2 for value in values]
    return expected_value_discrete(new_values, probabilities)
    

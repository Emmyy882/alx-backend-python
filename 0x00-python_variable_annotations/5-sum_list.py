#!/usr/bin/env python3
"""
type-annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a list input_list of floats as argument and returns their sum as a float.
    """
    return float(sum(input_list))

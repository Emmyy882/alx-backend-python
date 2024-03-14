#!/usr/bin/env python3
"""
implements a type-annotated function
"""
from typing import List, Union, Optional


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums the elements of the list and returns the sum in float"""
    return sum(mxd_lst)

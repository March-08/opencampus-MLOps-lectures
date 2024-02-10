"""
Module providing a function for computing gifts costs

Author: Marcello
Date: February 2024
"""


import numpy as np


def calculate_gift_costs(gift_costs_pth):
    '''
    This funciton compute the sum cost of all gift which cost is < 25

    Args:
    gift_costs_pth: (str) path of txt file containing gift data

    Returns:
    total_price: (int) sum of all gift cost that are z 25
    '''

    with open(gift_costs_pth, encoding='UTF-8') as file_in:
        gift_costs = file_in.read().split('\n')

    #change from string to int
    gift_costs = np.array(gift_costs).astype(int)  # convert string to int
    
    #compute total price + tax
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

    return total_price


if __name__ == "__main__":
    GIFT_COSTS = calculate_gift_costs("autopep8-and-pylint/gift_costs.txt")
    print(GIFT_COSTS)

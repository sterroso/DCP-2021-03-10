'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two 
numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true 
since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
from typing import List


def is_the_sum_of_two(k: int, list_of_numbers: List[int]) -> bool:
    # The list of numbers **must** have, at least, two elements.
    if len(list_of_numbers) <= 1:
        return False
    
    for i in range(len(list_of_numbers) - 1):
        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[i] + list_of_numbers[j] == k:
                return True
    
    return False


if __name__ == "__main__":
    k = 17
    l = list([10, 15, 3, 7])
    print('Is {} the sum of two in {}?'.format(k, l))
    print('{}'.format(is_the_sum_of_two(k, l)))
    
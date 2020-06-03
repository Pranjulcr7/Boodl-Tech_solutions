"""
Assumptions:
    1. Array is not sorted
    2. Return none if no solution exists

Algorithm:
    1. Making list of (value, index) pairs and sorting them according to value
    2. Using two pointers left and right, with initial n 0 and length of array - 1,
     to traverse the array.
    3. While left < right :
        a. if sum of left and right = target:
           return index of left and right elements
        b. else if sum < target:
           increment left so that current sum increases
        c. else if sum > target:
           decrement right to decrease current sum
    4.return result

Time complexity : O(n*log(n)) # sorting: n*log(n) + solution: n

Space complexity : O(n) #using new variable to for sorted array else O(1)
"""


def sum_to_n(elements: list, target: int):
    """
    This function returns the index of the elements that
    curr_sum equal to target n
    :param elements: list of integers
    :param target: integer
    :return: list of two integers
    """

    # making (value, index) pairs and sorting according value 
    sorted_elements = sorted(
        [{'value': value, 'index': index} for index, value in enumerate(elements)],
        key=lambda x: x.get('value')
    )

    # left and right pointer 
    left, right = 0, len(elements) - 1

    # result variable
    result = None

    while left < right:

        curr_sum = sorted_elements[left].get('value') + sorted_elements[right].get('value')

        if curr_sum == target:
            result = [
                sorted_elements[left].get('index'),
                sorted_elements[right].get('index')
            ]
            break

        elif curr_sum < target:
            left += 1

        else:
            right -= 1

    return result

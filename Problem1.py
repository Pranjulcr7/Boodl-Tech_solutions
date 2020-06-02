"""
Assumptions:
    1. Array is not sorted
    2. Return none if no solution exists

Algorithm:
    1. Making list of (n, index) pairs and sorting them according to n
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

"""


def sum_to_n(elements: list, target: int):
    """
    This function returns the index of the elements that
    curr_sum equal to target n
    :param elements: list of integers
    :param target: integer
    :return: list of two integers
    """

    sorted_elements = sorted(
        [{'n': value, 'index': index} for index, value in enumerate(elements)],
        key=lambda x: x.get('n')
    )
    left, right = 0, len(elements) - 1
    result = None

    while left < right:

        curr_sum = sorted_elements[left].get('n') + sorted_elements[right].get('n')

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

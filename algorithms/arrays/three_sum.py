"""
Given an array S of n integers, are there three distinct elements
a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
"""


def three_sum(array):
    """
    :param array: List[int]
    :return: Set[ Tuple[int, int, int] ]
    """

    res = set()
    array.sort()
    branch_array = [False] * 11
    for i in range(len(array) - 2):
        branch_array[0] = True
        if i > 0 and array[i] == array[i - 1]:
            if i > 0:
                branch_array[1] = True
            if array[i] == array[i - 1]:
                branch_array[2] = True
            continue
        l, r = i + 1, len(array) - 1
        while l < r:
            branch_array[3] = True
            s = array[i] + array[l] + array[r]
            if s > 0:
                branch_array[4] = True
                r -= 1
            elif s < 0:
                branch_array[5] = True
                l += 1
            else:
                branch_array[6] = True
                # found three sum
                res.add((array[i], array[l], array[r]))

                # remove duplicates
                while l < r and array[l] == array[l + 1]:
                    if l < r:
                        branch_array[7] = True
                    if array[l] == array[l + 1]:
                        branch_array[8] = True
                    l += 1

                # is this even run?
                while l < r and array[r] == array[r - 1]:
                    if l < r:
                        branch_array[9] = True
                    if array[r] == array[r - 1]:
                        branch_array[10] = True
                    r -= 1

                l += 1
                r -= 1
    return res, branch_array

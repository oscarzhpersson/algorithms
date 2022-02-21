"""
   This function takes two lists and returns the node they have in common, if any.
   In this example:
   1 -> 3 -> 5
               \
                7 -> 9 -> 11
               /
   2 -> 4 -> 6
   ...we would return 7.
   Note that the node itself is the unique identifier, not the value of the node.
   """
import unittest


class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def listCatchup(short, long, list):
        while(long > short):
            list = list.next
            long -= 1

        return (list, long)

def generateFlag(count, h1, h2):
    if h1.next is None or h2.next is None:
        return (count, h1.next, h2.next)

def getNext(h):
    if h:
        h = h.next
    return h

def intersection_Refactored(h1, h2):

    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    while h1 or h2:
        count += 1

        # We hit the end of one of the lists, set a flag for this
        if not flag:
            flag = generateFlag(count, h1, h2)

        h1 = getNext(h1)
        h2 = getNext(h2)

    long_len = count    # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None:
        shorter = h1_orig
        longer = h2_orig
    elif flag[2] is None:
        shorter = h2_orig
        longer = h1_orig

    while longer and shorter:

        longer, long_len = listCatchup(short_len, long_len, longer)

        if longer == shorter:
            # The nodes match, return the node
            return longer
        
        longer = longer.next
        shorter = shorter.next

    return None


class TestSuite(unittest.TestCase):

    def test_intersection(self):

        # create linked list as:
        # 1 -> 3 -> 5
        #            \
        #             7 -> 9 -> 11
        #            /
        # 2 -> 4 -> 6
        a1 = Node(1)
        b1 = Node(3)
        c1 = Node(5)
        d = Node(7)
        a2 = Node(2)
        b2 = Node(4)
        c2 = Node(6)
        e = Node(9)
        f = Node(11)

        a1.next = b1
        b1.next = c1
        c1.next = d
        a2.next = b2
        b2.next = c2
        c2.next = d
        d.next = e
        e.next = f

        self.assertEqual(7, intersection_Refactored(a1, a2).val)


if __name__ == '__main__':

    unittest.main()

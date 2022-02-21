"""


   Implements a manual coverage test for  ./intersection.py.


   """
import unittest


flags = {
    "flag0" : False,
    "flag1-while-h1" : 0,
    "flag1-while-h2" : 0,
    "flag2" : False,
    "flag3" : False,
    "flag4" : False,
    "flag5" : False,
    "flag6" : False,
    "flag7-while" : False,
    "flag8-while" : 0,
    "flag9" : 0,
    "flag10-else" : False,
}
    

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def intersection(h1, h2):

    flags["flag0"] = True # ! Unsure if this should be here. Disable if not. Complexity is now 19 with this, whereas lizard gave 18.

    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    while h1 or h2:

        if h1:
            flags["flag1-while-h1"] += 1 # ? Increment flag!
        
        if h2:
            flags["flag1-while-h2"] += 1 # ? Increment flag!

        count += 1

        if not flag and (h1.next is None or h2.next is None):
            flags["flag2"] = True # ? Set flag!
            # We hit the end of one of the lists, set a flag for this
            flag = (count, h1.next, h2.next)

        if h1:
            flags["flag3"] = True # ? Set flag!
            h1 = h1.next
            
        if h2:
            flags["flag4"] = True # ? Set flag!
            h2 = h2.next
            

    long_len = count    # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None:
        flags["flag5"] = True # ? Set flag!
        shorter = h1_orig
        longer = h2_orig
        
    elif flag[2] is None: # List 1 has a next element, but List 2 has no more elements.
        # ! Never reached.
        flags["flag6"] = True # ? Set flag!
        shorter = h2_orig
        longer = h1_orig
        

    while longer and shorter:

        flags["flag7-while"] += 1 # ? Increment flag!

        while long_len > short_len:

            # ! Never reached.
            flags["flag8-while"] += 1 # ? Increment flag!

            # force the longer of the two lists to "catch up"
            longer = longer.next
            long_len -= 1

        if longer == shorter:
            flags["flag9"] = True # ? Set flag!
            # The nodes match, return the node
            return longer
        else:
            flags["flag10-else"] = True # ? Set flag!
            longer = longer.next
            shorter = shorter.next

    return None

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

        assert(intersection(a1, a2).val == 7)

        #self.assertEqual(7, intersection(a1, a2).val)

# Added test which runs the branches that the previous test did not run.
    # When there are no matching nodes.
    # When one list is longer than the other before the element is found. (Asymmetry)

if __name__ == '__main__':

    test_intersection(unittest.TestCase)

    for index, (key, val) in enumerate(flags.items()):
        print(f'Index: {index}, Key: {key}, Value: {val}')

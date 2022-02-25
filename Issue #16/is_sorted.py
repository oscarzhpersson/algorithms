"""
Given a linked list, is_sort function returns true if the list is in sorted
(increasing) order and return false otherwise. An empty list is considered
to be sorted.

For example:
Null :List is sorted
1 2 3 4 :List is sorted
1 2 -1 3 :List is not sorted
"""

flags = {
    "flag0" : False,
    "flag1-while" : 0,
    "flag2" : False,
    }

def is_sorted(head):

    if not head:

        flags["flag0"] = True # ! Never run! FIXED.

        for index, (key, val) in enumerate(flags.items()):
            print(f'Index: {index}, Key: {key}, Value: {val}')
        return True

    current = head
    while current.next:

        flags["flag1-while"] += 1

        if current.val > current.next.val:
            flags["flag2"] = True

            for index, (key, val) in enumerate(flags.items()):
                print(f'Index: {index}, Key: {key}, Value: {val}')
            return False
        current = current.next

    for index, (key, val) in enumerate(flags.items()):
        print(f'Index: {index}, Key: {key}, Value: {val}')
    return True

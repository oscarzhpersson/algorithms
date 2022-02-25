"""
In this function, the for-loop signified by the flag "flag4-for" is never run. A test has been added to ammend this.
"""

flags = {
    "flag0" : False,
    "flag1-for" : 0,
    "flag2" : False,
    "flag3-else" : False,
    "flag4-for" : 0,
    "flag5-for" : 0,
    "flag6" : False,
    }

def remove_range(head, start, end):
    assert(start <= end)
    # Case: remove node at head
    if start == 0:

        flags["flag0"] = True

        for i in range(0, end+1):

            flags["flag1-for"] += 1

            if head != None:

                flags["flag2"] = True

                head = head.next
    else:

        flags["flag3-else"] = True

        current = head
        # Move pointer to start position
        for i in range(0,start-1):

            flags["flag4-for"] += 1 # ! Never run! Finish this and do another function.

            current = current.next
        # Remove data until the end
        for i in range(0, end-start + 1):

            flags["flag5-for"] += 1

            if current != None and current.next != None:

                flags["flag6"] = True

                current.next = current.next.next
    
    
    for index, (key, val) in enumerate(flags.items()):
        print(f'Index: {index}, Key: {key}, Value: {val}')

    return head

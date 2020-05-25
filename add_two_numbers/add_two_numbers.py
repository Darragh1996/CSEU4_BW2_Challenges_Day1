"""
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }


 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
"""


class ListNode:
    def __init__(self, val, nex=None):
        self.value = val
        self.next = nex

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, current_next)


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_tail(self, value):
        self.tail.insert_after(value)
        self.tail = self.tail.next


def create_list(num):
    """
    create a linked list from an int
    """
    num = str(num)
    num = num[::-1]

    new_node = ListNode(int(num[0]))
    l = LinkedList(new_node)
    print(l.head)
    for i in range(1, len(num)):
        l.add_to_tail(num[i])

    return l


def addTwoNumbers(l1, l2):
    l1_curr = l1.head
    l2_curr = l2.head
    l1_num = ""
    l2_num = ""

    # iterate through the link list
    while l1_curr != None:
        # add each value to a string
        l1_num += str(l1_curr.value)
        l1_curr = l1_curr.next
    # reverse the order of the string as values are stored in reverse order
    l1_num = int(l1_num[::-1])

    # same as above
    while l2_curr != None:
        l2_num += str(l2_curr.value)
        l2_curr = l2_curr.next
    l2_num = int(l2_num[::-1])

    # add the nums
    l_sum = l1_num + l2_num

    return create_list(l_sum)


# test
l1 = create_list(342)
l2 = create_list(465)

test = addTwoNumbers(l1, l2)
curr = test.head
while curr != None:
    print(curr.value)
    curr = curr.next

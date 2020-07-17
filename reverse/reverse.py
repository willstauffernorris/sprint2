class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        
        #takes care of the first two reverse
        print(f'HEAD {node}')
        if (node == None) or (node.next_node == None):
            return node

#--------
#this almost works
        the_next_node = node.next_node
        print(the_next_node.value)

        reversed_list = node
        reversed_list.next_node = None
        print(reversed_list.value)

        while the_next_node != None:
            print(the_next_node.value)
            temp = the_next_node
            next_node = the_next_node.next_node

            temp.next_node = reversed_list
            reversed_list = temp
        
        return reversed_list


        #___________

        #     temp.next_node = reversed_list
        #     reversed_list = temp
        # return reversed_list




        # reversed_list_1 = reverse_list(node.next_node, None)
        # node.next_node.next_node = self.head
        # node.next_node = None
        # return reversed_list_1

        # list_to_do = self.head.next_node

        # reversed_list = self.head
        # reversed_list.next_node = None

        # while list_to_do != None:
        #     temp = list_to_do
        #     list_to_do = list_to_do.next_node

        #     temp.next_node = reversed_list
        #     reversed_list = temp

        # return reversed_list
        
        
        # # #prev = None
        # current = self.head
        
        # while (current is not None):
        #     current.next_node = prev
        #     prev = current
        #     current = current.next_node
        #     print(current)
        # self.head = prev
        
        # if node.next_node is None:
        #     return node
        


        # rest = self.reverse_list(self.head.next)

        # self.head.next.next = head
        # self.head.next = None

        # return rest


        # current = self.head
        # while current is not None:
        #     pass



'''
Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List. _Without_ making it a Doubly Linked List (adding a tail attribute), complete the `reverse_list()` function within `reverse/reverse.py` 
reverse the contents of the list using recursion, *not a loop.*

For example,
```
1->2->3->None
```
would become...
```
3->2->1->None
```
'''
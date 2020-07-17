class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer_storage = []
        self.counter = 0
        
        #pass

    def append(self, item):
        '''The `append` method adds the given element to the buffer.'''
        #print(self.buffer_storage)

        #print(len(self.buffer_storage))

        if self.capacity > (len(self.buffer_storage)):
            self.buffer_storage.append(item)
            #print(self.buffer_storage)
            self.counter += 1
            #print(self.counter)
        # # if self.capacity >= len(buffer_storage):
        else:
            #counter_reset
            if self.counter == self.capacity:
                self.counter = self.counter - self.capacity
            self.buffer_storage[self.counter] = item
            self.counter += 1
        #     i += 1
            #pass

    def get(self):
        '''The `get` method returns all of the elements in the buffer in a list in their given order.
        It should not return any `None` values in the list even if they are present in the ring buffer.'''
        # if len(buffer_storage) == 0:
        #     return buffer_storage
        return self.buffer_storage
        pass



'''
    For example:

```python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
```
'''
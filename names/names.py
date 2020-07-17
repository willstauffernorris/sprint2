#*You may not use the built in Python list, set, or dictionary in your solution for this problem. 
#  However, you can and should use the provided `duplicates` list to return your solution.*
#(Hint: You might try importing a data structure you built during the week)


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)
        #pass

    def enqueue(self, value):
        return self.storage.insert(0, value)
        #pass

    def dequeue(self):
        if len(self.storage) >= 1:
            return self.storage.pop(-1)



import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


## The complexity is O(n*n)


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



## Not sure if this is allowed or not, but it's only 1 second runtime
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)



## Basically the same thing, 1.08 seconds
queue = Queue()

for name1 in names_1:
    queue.enqueue(name1)
for name2 in names_2:
    if name2 in queue.storage:
        duplicates.append(name2)


## This is not a good solution
# i=0
# for name1 in names_1:
#     queue.enqueue(name1)

# while i <= len(queue):
#     for name2 in names_2:
#         if name2 == queue.storage[i]:
#             duplicates.append(name2)
#             i+=1


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.



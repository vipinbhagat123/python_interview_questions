# What is an Iterator in Python?

# An iterator is an object in Python that allows you to traverse through all the elements of a collection (like a list or tuple) one at a time, without using indexing.



my_list = [10, 20, 30]
iterator = iter(my_list)   # or: my_list.__iter__()

print(next(iterator))      # or: iterator.__next__() → 10
print(next(iterator))      # → 20
print(next(iterator))      # → 30
# print(next(iterator))    # Raises StopIteration

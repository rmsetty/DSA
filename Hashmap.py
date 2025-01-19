class HashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [None for i in range(self.max)]

    def hash_function(self, key):
        index = 0
        for char in key:
            index += ord(char) % self.MAX
        return index

    def set_item(self, key, value):
       index = self.hash_function(key)
       self.array[index] = value

    def get_item(self, key):
        index = self.hash_function(key)
        return self.array[index]

    def delete_item(self, key):
        index = self.hash_function(key)
        self.array[index] = None



class SeparateChainingHashTable:
    def __init__(self):
        self.size = 10
        self.array = [[] for_in range(self.size)]

    def hash_function(self, key):
        index = 0
        for char in key:
            index += ord(char) % self.size
        return index

    def set_item(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in self.array[index]:
            if k == key:
                self.array[index][i] = (key, value)
                return
        self.array[index].append((key, value))

    def get_item(self, key):
        index = self.hash_function(key)
        for (k, v) in self.array[index]:
            if k == key
                return v
        return None

    def delete_item(self, key):
        index = self.hash_function(key)
        for i, (k, v) in self.array[index]:
            if k == key:
                del self.array[index][i]
                return



class LinearProbingHashTable:
    def __init__(self):
        self.size = 10
        self.array = [None for i in range(self.size)]

    def hash_function(self, key):
        index = 0
        for char in key:
            index += ord(char) % self.size
        return index

    def set_item(self, key, value):
        index = self.hash_function(key)
        while self.array[index] is not None:
            if self.array[index][0] == key:
                self.array[index][1]==value
                return
            index = (index + 1) % self.size
        self.array[index] = (key, value)

    def get_item(self, key):
        index = self.hash_function(key)
        while self.array[index] is not None
            if (self.array[index][0] ==key):
                return self.array[index][1]
            index = (index + 1) % self.size
        return None


    def delete_item(self, key):
        index = self.hash_function(key)
        while self.array[index] is not None:
            if self.array[index][0] == key:
                self.array[index] = None
                return
            index = (index + 1) % self.size
        return 


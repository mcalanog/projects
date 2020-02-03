class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        horner = self.horner_hash(key)
        hornernew = horner
        a = 0
        while True:
            if self.hash_table[hornernew] is None:
                self.hash_table[hornernew] = [key, {value}]
                self.num_items += 1
                break
            elif self.hash_table[hornernew][0] == key:
                self.hash_table[hornernew][1].add(value)
                break
            hornernew = (horner + a ** 2) % self.table_size
            a += 1
        if self.num_items / self.table_size > .5:
            self.resize()

    def resize(self):
        old= self.hash_table
        oldsize = self.table_size
        self.table_size = oldsize * 2 + 1
        self.hash_table = [None] * self.table_size
        self.num_items = 0
        for item in old:
            if item is not None:
                self.insert_resize(item[0], item[1])


    def insert_resize(self, key, value):
        horner = self.horner_hash( key )
        hornernew = horner
        a = 0
        while self.hash_table[hornernew] is not None:
            hornernew = (horner + a ** 2)% self.table_size
            a += 1
        self.hash_table[hornernew] = [key, value]
        self.num_items += 1


    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        if len(key) < 8:
            n = len(key)
        else:
            n = 8
        horner = 0
        indx = 0
        while indx < n:
            letter = key[indx]
            horner += (ord(letter) * (31 ** (n - 1 - indx)))
            indx += 1
        return horner % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        if self.get_index(key) is None:
            return False
        return True

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key.
        If there is not an entry with the provided key, returns None."""
        a = 0
        index = self.horner_hash(key)
        indexnew = index
        while self.hash_table[indexnew] is not None and self.hash_table[indexnew][0]!= key:
            indexnew = (index + a ** 2) % self.table_size
            a += 1
        if self.hash_table[indexnew] is None:
            return None
        return indexnew


    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        thelist= list(filter(None, self.hash_table))
        other = []
        for item in thelist:
            other += [item[0]]
        return other

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key.
        If key is not in hash table, returns None."""
        index = self.get_index(key)
        if index is not None:
            mylist = list(self.hash_table[index][1])
            mylist.sort()
            return mylist

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size
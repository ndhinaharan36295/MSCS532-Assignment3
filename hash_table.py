class HashTable:
    def __init__(self, size=5):
        # Initialize the hash table with a given size
        self.size = size
        # Create empty buckets for storing key-value pairs
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        # Compute the hash index for a given key
        # Uses Python's built-in hash function and modulo operation
        return hash(key) % self.size

    # Inserts a key-value pair into the hash table
    def insert(self, key, value):
        # Gets the hash index for the key
        index = self._hash(key)
        # Access the corresponding bucket
        bucket = self.buckets[index]

        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Updates existing key
                return

        # Adds the new key-value pair to the bucket
        bucket.append((key, value))
        self.count += 1

        # Resize hash-table if load factor exceeds threshold
        if self.load_factor() > 0.75:
            self._resize()

    # Searches for a value associated with a given key
    def search(self, key):
        # Gets the hash index for the key
        index = self._hash(key)
        # Access the corresponding bucket
        bucket = self.buckets[index]

        # Iterate through the bucket to find the key
        for k, v in bucket:
            if k == key:
                return v    # Returns the value if the key is found
        return None         # Return None if the key is not found

    # Deletes a key-value pair from the hash table
    def delete(self, key):
        # Gets the hash index for the key
        index = self._hash(key)
        # Access the corresponding bucket
        bucket = self.buckets[index]

        # Iterate through the bucket to find the key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Removes the key-value pair from the bucket
                del bucket[i]
                # Decreases the count of elements
                self.count -= 1
                return True
        return False

    # Calculates the load factor of the hash table
    # Load factor = number of elements / size of the hash table
    def load_factor(self):
        return self.count / self.size

    # Resizes the hash table when the load factor exceeds the threshold
    def _resize(self):
        # Doubles the size of the hash table
        new_size = self.size * 2
        # Creates a new hash table with the new size
        new_table = HashTable(new_size)

        # Rehash all key-value pairs into the new hash table
        for bucket in self.buckets:
            for key, value in bucket:
                new_table.insert(key, value)

        # Update the current hash table with the new table's attributes
        self.size = new_table.size
        self.buckets = new_table.buckets
        self.count = new_table.count

    def __str__(self):
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.buckets))

if __name__ == "__main__":
    ht = HashTable()

    ht.insert(3, "apple")
    ht.insert(5, "orange")  # Update existing key
    print("\nAfter inserts:")
    print(ht)

    print("\nSearch for key '5':", ht.search(5))
    print("Search for key '10':", ht.search(10))

    ht.delete(3)

    print("\nAfter delete:")
    print(ht)

    print("\nLoad Factor:", ht.load_factor())


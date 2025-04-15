class HashTable:
    def __init__(self, rosmir=10, load_factor=0.7):
        self.rosmir = rosmir
        self.size = 0
        self.load_factor = load_factor
        self.table = [None] * rosmir

    def _hash(self, key):
        return hash(key) % self.rosmir

    def _resize(self):
        old_table = self.table
        self.rosmir *= 2
        self.table = [None] * self.rosmir
        self.size = 0

        for item in old_table:
            if item is not None:
                self._insert(item[0], item[1])

    def _insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.rosmir

        self.table[index] = (key, value)
        self.size += 1

        if self.size / self.rosmir > self.load_factor:
            self._resize()

    def add(self, key, value):
        self._insert(key, value)

    def get(self, key):
        index = self._hash(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.rosmir

        raise KeyError('Ключ не знайдено')

    def __repr__(self):
        return str([item for item in self.table if item is not None])


hash_table = HashTable()
hash_table.add("name", "Дмитро")
hash_table.add("language", "Українська")
hash_table.add("old", "15")

print(hash_table)
print("name", hash_table.get('name'))
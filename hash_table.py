class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.count = 0
        self.array = [DoublyLinkedList() for _ in range(size)]
    
    def hash_function(self, key):
        A = 0.6180339887  
        return int(self.size * ((key * A) % 1))
    
    def insert(self, key, value):
        index = self.hash_function(key)
        list_at_index = self.array[index]
        for node in list_at_index:
            if node.key == key:
                node.value = value
                return
        list_at_index.append(key, value)
        self.count += 1
        if self.count > self.size * 2:  
            self._resize(2 * self.size)
    
    def get(self, key):
        index = self.hash_function(key)
        list_at_index = self.array[index]
        for node in list_at_index:
            if node.key == key:
                return node.value
        return None
    
    def remove(self, key):
        index = self.hash_function(key)
        list_at_index = self.array[index]
        for node in list_at_index:
            if node.key == key:
                list_at_index.remove(node)
                self.count -= 1
                if self.count < self.size // 4: 
                    self._resize(self.size // 2)
                return
    
    def _resize(self, new_size):
        old_array = self.array
        self.size = new_size
        self.array = [DoublyLinkedList() for _ in range(new_size)]
        self.count = 0  
        for linked_list in old_array:
            for node in linked_list:
                self.insert(node.key, node.value)


hash_table = HashTable()
hash_table.insert(5, 10)
hash_table.insert(8, 15)
hash_table.insert(10, 12)
hash_table.insert(20, 47)
hash_table.insert(30, 23)
print(hash_table.get(20))
hash_table.remove(20)
print(hash_table.get(20))
print(hash_table.get(5))  
print(hash_table.get(8))  
print(hash_table.get(30))
hash_table.remove(5)
print(hash_table.get(5))  

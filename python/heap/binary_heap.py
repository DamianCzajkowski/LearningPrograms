class Heap:

    def __init__(self, max_size):
        self.custom_list = (max_size + 1) * [None]
        self.size = 0
        self.max_size = max_size + 1

    def peek(self):
        return self.custom_list[1]

    def __str__(self):
        str_value = []
        for i in range(1, self.size+1):
            str_value.append(str(self.custom_list[i]))
        return " ".join(str_value)

    def replace_with(self, index, replace_index):
        temp_value = self.custom_list[index]
        self.custom_list[index] = self.custom_list[replace_index]
        self.custom_list[replace_index] = temp_value

    def heapify_insert(self, index, heap_type):
        parent_index = index//2

        if index <= 1:
            return
        if (heap_type == 'Min' and self.custom_list[parent_index] > self.custom_list[index]) or \
                (heap_type == "Max" and self.custom_list[parent_index] < self.custom_list[index]):
            self.replace_with(index, parent_index)
            self.heapify_insert(parent_index, heap_type)

    def heapify_extract(self, index, heap_type):
        left_index = index*2
        right_index = index*2 + 1
        swap_child = 0
        if self.size < left_index:
            return
        if self.size == left_index:
            if (heap_type == "Min" and self.custom_list[index] > self.custom_list[left_index]) or\
                    (heap_type == "Max" and self.custom_list[index] < self.custom_list[left_index]):
                self.replace_with(index, left_index)
        else:
            if heap_type == "Min":
                if self.custom_list[left_index] < self.custom_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.custom_list[index] > self.custom_list[swap_child]:
                    self.replace_with(index, swap_child)
            elif heap_type == "Max":
                if self.custom_list[left_index] > self.custom_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.custom_list[index] < self.custom_list[swap_child]:
                    self.replace_with(index, swap_child)
            self.heapify_extract(swap_child, heap_type)

    def insert(self, node_value, heap_type="Min"):
        if self.size + 1 == self.max_size:
            return "Heap is full"
        self.custom_list[self.size+1] = node_value
        self.size += 1
        self.heapify_insert(self.size, heap_type)
        return "Value inserted!"

    def extract(self, heap_type="Min"):
        if self.size == 0:
            return
        extracted_node = self.custom_list[1]
        self.custom_list[1] = self.custom_list[self.size]
        self.custom_list[self.size] = None
        self.size -= 1
        self.heapify_extract(1, heap_type)
        return extracted_node

    def delete(self):
        self.custom_list = None
        self.size = 0


b_heap = Heap(10)
# b_heap.insert(3)
# b_heap.insert(4)
# b_heap.insert(6)
# b_heap.insert(1)
# b_heap.insert(8)
# b_heap.insert(5)
b_heap.insert(4, "Max")
b_heap.insert(5, "Max")
b_heap.insert(2, "Max")
b_heap.insert(1, "Max")

print(b_heap)
print(b_heap.extract("Max"))
print(b_heap)

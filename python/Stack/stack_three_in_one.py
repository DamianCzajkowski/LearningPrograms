class MultiStack:

    def __init__(self, stack_size):
        self.number_stacks = 3
        self.custlist = [0] * (stack_size * self.number_stacks)
        self.sizes = [0] * self.number_stacks
        self.stack_size = stack_size

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def index_of_top(self, stack_num):
        offset = (stack_num * self.number_stacks)
        return offset + self.stack_size[stack_num] - 1

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            return "This stack is full"
        stack_top_index = self.index_of_top(stack_num)
        self.custlist[stack_top_index] = item
        self.sizes[stack_num] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return "This stack is empty"
        stack_top_index = self.index_of_top(stack_num)
        result = self.custlist[stack_top_index]
        self.custlist[stack_top_index] = 0
        self.sizes[stack_num] -= 1
        return result

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return "This stack is empty"
        stack_top_index = self.index_of_top(stack_num)
        return self.custlist[stack_top_index]

class Stack:
    def __init__(self):
        self.el = []
        self.length: int = 0

    def get_length(self) -> int:
        return self.length

    def push(self, item):
        self.el.append(item)
        self.length += 1

    def pop(self):
        if self.get_length() == 0:
            return -1
        else:
            return self.el.pop()

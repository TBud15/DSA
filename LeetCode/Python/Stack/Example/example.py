class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def size(self):
        return len(self.items)

# Создаем экземпляр стека
stack = Stack()

# Демонстрируем использование методов push, pop и peek
# Добавляем элементы в стек
stack.push(1)
stack.push(2)
stack.push(3)

# Просматриваем верхний элемент стека
peek_element = stack.peek()

# Удаляем элемент из стека
popped_element = stack.pop()

# Выводим результаты
peek_element, popped_element, stack.items


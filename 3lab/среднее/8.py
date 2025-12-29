class Counter:
    
    def __init__(self, start=0):
        self.value = start
    
    def increment(self):
        self.value += 1
    
    def decrement(self):
        self.value -= 1
    
    def get_value(self):
        return self.value

counter = Counter(5)
print(counter.get_value())
counter.increment()
print(counter.get_value())
counter.increment()
print(counter.get_value())
counter.decrement()
print(counter.get_value()) 
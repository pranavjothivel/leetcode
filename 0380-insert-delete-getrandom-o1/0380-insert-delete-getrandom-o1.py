class RandomizedSet:

    def __init__(self):
        self.internal_set = set()
        self.internal_list = []

    def insert(self, val: int) -> bool:
        if val in self.internal_set:
            return False
        self.internal_set.add(val)
        self.internal_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.internal_set:
            return False
        self.internal_set.remove(val)
        
        index = self.internal_list.index(val)
        last = self.internal_list[-1]
        self.internal_list[index] = last
        self.internal_list.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.internal_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
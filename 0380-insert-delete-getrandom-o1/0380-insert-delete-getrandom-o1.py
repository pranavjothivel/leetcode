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
        self.internal_list.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.internal_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
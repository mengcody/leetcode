import random


class RandomizedSet:
    def __init__(self):
        # num contains all the input values
        self.num = []
        # key: val
        # val: val index in num
        self.set = dict()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False

        self.num.append(val)
        self.set[val] = len(self.num)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False

        # swap the val to the end
        last_element = self.num[-1]
        index_to_remove = self.set[val]

        self.num[index_to_remove] = last_element
        self.set[last_element] = index_to_remove

        # delete the val
        self.num.pop()
        del self.set[self.num[-1]]

    def get_random(self) -> int:
        return random.choice(self.num)


if __name__ == "__main__":
    pass

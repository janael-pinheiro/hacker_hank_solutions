from functools import cmp_to_key


class Checker:
    @staticmethod
    def compare(p1, p2):
        if p1.score == p2.score:
            if p1.name == p2.name:
                return 0
            elif p1.name > p2.name:
                return 1
            else:
                return -1
        elif p1.score < p2.score:
            return 1
        else:
            return -1


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    @staticmethod
    def comparator(a, b):
        return Checker.compare(a, b)


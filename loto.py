# ----- Ваша карточка ------
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11    14  -    87
#       16 49    55 77    88
#    15 20        -    76  -
# --------------------------

from random import sample, shuffle


class Card:

    pool = [el for el in range(1, 91)]

    def __init__(self):
        shuffle(Card.pool)
        str_1 = Card.pool[:6]
        str_2 = Card.pool[6:11]
        str_3 = Card.pool[11:16]
        self.lst = [Card.place(str_1), Card.place(str_2), Card.place(str_3)]

    @staticmethod
    def place(nums):
        nums.sort()
        str_0 = ["  " for _ in range(9)]
        index_str = sample([el for el in range(9)], 5)
        index_str.sort()
        for i, el in enumerate(index_str):
            str_0[el] = nums[i]
        return str_0

    def cross_out(self, n):
        for i, el in enumerate(self.lst):
            for j, num in enumerate(el):
                if num == n:
                    self.lst[i][j] = " -"
                    break
        return self.lst


class UserCard(Card):

    def __str__(self):
        card = "\n".join([" ".join([str(num) for num in el]) for el in self.lst])
        return f"----- Ваша карточка ------\n{card}\n--------------------------"


class ComputerCard(Card):

    def __str__(self):
        card = "\n".join([" ".join([str(num) for num in el]) for el in self.lst])
        return f"-- Карточка компьютера ---\n{card}\n--------------------------"


a = UserCard()
c = ComputerCard()

print(a)
print(c)

lot = 15
a.cross_out(lot)
c.cross_out(lot)

print(a)
print(c)

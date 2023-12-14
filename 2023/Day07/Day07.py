from test import star_one, star_two, example
from collections import Counter, deque
from enum import Enum


class Hand(Enum):
    HIGH = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEKIND = 4
    FULLHOUSE = 5
    FOURKIND = 6
    FIVEKIND = 7


def map_card_to_num(card, star_two=False):
    if card.isdigit():
        return int(card)
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "T":
        return 10

    return 1 if star_two else 11


class Solution:
    # Star 1
    """
    Notes:
    """

    def parse_input(self, input):
        print(f"Use if required {input}")

    # return hand type given string
    def get_hand(self, hand, star_two=False):
        counts = Counter(hand)
        if len(counts) == 1:
            return Hand.FIVEKIND

        max_same = max(counts.values())
        j_counts = counts["J"]

        # four kind full house
        if len(counts) == 2:
            if max_same == 4:
                if star_two and j_counts:
                    return Hand.FIVEKIND

                return Hand.FOURKIND
            else:
                if star_two and j_counts:
                    return Hand.FIVEKIND

                return Hand.FULLHOUSE

        # three of kind two pair
        if len(counts) == 3:
            max_same = max(counts.values())
            if max_same == 3:
                if star_two and j_counts:
                    return Hand.FOURKIND
                return Hand.THREEKIND
            else:
                if star_two:
                    if j_counts == 1:
                        return Hand.FULLHOUSE
                    if j_counts == 2:
                        return Hand.FOURKIND
                return Hand.TWOPAIR

        if len(counts) == 4:
            if star_two and j_counts:
                return Hand.THREEKIND
            return Hand.ONEPAIR

        if star_two and j_counts:
            return Hand.ONEPAIR
        return Hand.HIGH

    def compare_hands(self, cur, hand, star_two=False):
        for x, y in zip(cur, hand):
            x_val = map_card_to_num(x, star_two)
            y_val = map_card_to_num(y, star_two)
            if x_val > y_val:
                return True
            elif x_val < y_val:
                break
        return False

    def star_one(self, input: str):
        if not input:
            return

        res = 0
        order = deque([])
        for line in input.splitlines():
            [hand, bid] = line.split()
            hand_type = self.get_hand(hand).value

            if not order:
                order.append((hand_type, hand, int(bid)))
                continue

            for index, val in enumerate(order):
                # if current hand is less the cur hands val we can insert into that position
                if val[0] > hand_type:
                    order.insert(index, (hand_type, hand, int(bid)))
                    break

                # if hand types are equal we need to asses strength based on cards in order
                if val[0] == hand_type:
                    if self.compare_hands(val[1], hand):
                        order.insert(index, (hand_type, hand, int(bid)))
                        break
            else:
                order.append((hand_type, hand, int(bid)))

        for index, val in enumerate(order):
            # print(index + 1, val)
            res += (index + 1) * val[2]

        print(f"Star 1: {res}")
        return res

    # Star 2
    """
    Notes:

    """

    def star_two(self, input):
        if not input:
            return
        res = 0

        order = deque([])
        for line in input.splitlines():
            [hand, bid] = line.split()
            hand_type = self.get_hand(hand, True).value

            if not order:
                order.append((hand_type, hand, int(bid)))
                continue

            for index, val in enumerate(order):
                # if current hand is less the cur hands val we can insert into that position
                if val[0] > hand_type:
                    order.insert(index, (hand_type, hand, int(bid)))
                    break

                # if hand types are equal we need to asses strength based on cards in order
                if val[0] == hand_type:
                    if self.compare_hands(val[1], hand, True):
                        order.insert(index, (hand_type, hand, int(bid)))
                        break
            else:
                order.append((hand_type, hand, int(bid)))

        for index, val in enumerate(order):
            res += (index + 1) * val[2]

        print(f"Star 2: {res}")
        return res


def main():
    print("Tests:")
    solution = Solution()
    solution.star_one(example)
    solution.star_one(
        """32T3K 765
T33J5 684"""
    )
    solution.star_two(example)
    solution.star_two("JJJJJ 1")
    solution.star_two("3311J 1")

    print("\n\nMain Solution:")
    sol_one = solution.star_one(star_one)
    sol_two = solution.star_two(star_two)
    print("Done!")


if __name__ == "__main__":
    main()

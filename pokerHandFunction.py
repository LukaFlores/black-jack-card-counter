from ultralytics import YOLO
import cv2
import cvzone
import math


def findHiLoCount(hand):

    ranks = []

    count = 0

    # Seperate into list of suits and ranks
    for card in hand:
        if len(card) == 2:
            rank = card[0]
        else:
            rank = card[0:2]

        # Convert High Ranks to Numbers
        if rank == "A":
            rank = 14
        if rank == "K":
            rank = 13
        if rank == "Q":
            rank = 12
        if rank == "J":
            rank = 11

        ranks.append(int(rank))

    for rank in ranks:
        if rank >= 10:
            count -= 1
        if 9 >= rank >= 7:
            count += 0
        if 6 >= rank >= 2:
            count += 1

    return count


if __name__ == "__main__":
    findHiLoCount(["AH", "KH", "QH", "JH", "10H"])  # Royal Flush
    findHiLoCount(["KH", "QH", "JH", "10H", "9H"])  # Straight Flush
    findHiLoCount(["5H", "5S", "5D", "5C", "9H"])  # Four of a Kind
    findHiLoCount(["5H", "5S", "5D", "9D", "9H"])  # Full House
    findHiLoCount(["KD", "QH", "JC", "10H", "9S"])  # Straight
    findHiLoCount(["KH", "8H", "3H", "9H", "2H"])  # Flush
    findHiLoCount(["5H", "5S", "5D", "8D", "9H"])  # Three of a kind
    findHiLoCount(["5H", "5S", "2D", "8D", "8H"])  # Two Pair
    findHiLoCount(["5H", "5S", "2D", "8D", "9H"])  # One Pair
    findHiLoCount(["4H", "5S", "2D", "8D", "9H"])  # High Card

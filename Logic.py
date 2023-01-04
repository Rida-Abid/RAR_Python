import sys
import random


class logic:
    def ReversedList(self, Words):
        Words.reverse()
        return Words

    def SortedList(self, Words):
        Words.sort()
        return Words

    def Randomise(self, Words):
        random.shuffle(Words)
        return Words

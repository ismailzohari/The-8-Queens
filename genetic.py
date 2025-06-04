import random

class Genetic8Queens:
    def __init__(self, board_size=8):
        self.board_size = board_size

    def generate_chromosome(self):
        """
        Generates a random chromosome (a permutation of numbers from 0 to 7).
        Each index represents a column and the value is the row of the queen.
        """
        chromosome = list(range(self.board_size))
        random.shuffle(chromosome)
        return chromosome

    def fitness(self, chromosome):
        """
        Calculates the number of non-attacking pairs of queens.
        The maximum number of non-attacking pairs is 28 (8 choose 2).
        """
        attacking_pairs = 0
        for i in range(len(chromosome)):
            for j in range(i + 1, len(chromosome)):
                if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                    attacking_pairs += 1
        return 28 - attacking_pairs  # 28 is total possible pairs in 8 elements

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
        """
        attacking_pairs = 0
        for i in range(len(chromosome)):
            for j in range(i + 1, len(chromosome)):
                if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                    attacking_pairs += 1
        return 28 - attacking_pairs

    def selection(self, population, fitnesses):
        """
        Selects two parents using tournament selection.
        """
        tournament_size = 3
        selected = []
        for _ in range(2):
            participants = random.sample(list(zip(population, fitnesses)), tournament_size)
            winner = max(participants, key=lambda x: x[1])
            selected.append(winner[0])
        return selected

    def crossover(self, parent1, parent2):
        """
        Performs single-point crossover between two parents.
        """
        point = random.randint(1, self.board_size - 2)
        child = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
        return child

    def mutate(self, chromosome, mutation_rate=0.1):
        """
        Mutates the chromosome by swapping two genes with a given probability.
        """
        if random.random() < mutation_rate:
            i, j = random.sample(range(self.board_size), 2)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
        return chromosome

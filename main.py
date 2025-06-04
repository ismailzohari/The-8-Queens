from genetic import Genetic8Queens
from visualize import draw_chessboard

POPULATION_SIZE = 100
GENERATIONS = 1000

if __name__ == "__main__":
    solver = Genetic8Queens()

    # Step 1: Generate initial population
    population = [solver.generate_chromosome() for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        fitnesses = [solver.fitness(ch) for ch in population]

        # Check for solution
        if 28 in fitnesses:
            solution = population[fitnesses.index(28)]
            print(f"✅ Solution found at generation {generation}: {solution}")
            break

        # Step 2: Create next generation
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = solver.selection(population, fitnesses)
            child = solver.crossover(parent1, parent2)
            child = solver.mutate(child)
            new_population.append(child)

        population = new_population
    else:
        print("❌ No solution found.")
draw_chessboard(solution)
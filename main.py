from genetic import Genetic8Queens
from visualize import draw_chessboard
import matplotlib.pyplot as plt

POPULATION_SIZE = 100
GENERATIONS = 1000

if __name__ == "__main__":
    solver = Genetic8Queens()

    # Step 1: Generate initial population
    population = [solver.generate_chromosome() for _ in range(POPULATION_SIZE)]
    best_fitness_per_generation = []

    for generation in range(GENERATIONS):
        fitnesses = [solver.fitness(ch) for ch in population]
        best_fitness = max(fitnesses)
        best_fitness_per_generation.append(best_fitness)

        # Step 2: Check for solution
        if best_fitness == 28:
            solution = population[fitnesses.index(28)]
            print(f"✅ Solution found at generation {generation}: {solution}")
            draw_chessboard(solution)
            break

        # Step 3: Create next generation
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = solver.selection(population, fitnesses)
            child = solver.crossover(parent1, parent2)
            child = solver.mutate(child)
            new_population.append(child)

        population = new_population
    else:
        print("❌ No solution found.")

    # Step 4: Plot fitness progress
    plt.figure(figsize=(10, 5))
    plt.plot(best_fitness_per_generation, color='blue', linewidth=2)
    plt.title("Best Fitness per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Fitness Score")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("./Results/fitness_progress.png")
    plt.show()

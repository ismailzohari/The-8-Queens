from genetic import Genetic8Queens

if __name__ == "__main__":
    genetic_solver = Genetic8Queens()
    chromosome = genetic_solver.generate_chromosome()
    fitness = genetic_solver.fitness(chromosome)

    print(f"Generated Chromosome: {chromosome}")
    print(f"Fitness Score: {fitness} / 28")

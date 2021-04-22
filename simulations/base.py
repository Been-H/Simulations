class Simulation:

    def __init__(self, num_generations):
        self.num_generations = num_generations
        self.generation = 0
        self.generation_marks = []
        self.max_organisms = 0
        self.organisms = []
        self.num_organisms = []

    def setup(self, num_organisms, organism):
        for i in range(num_organisms):
            self.add_organism(organism)

    def run(self):
        for i in range(self.num_generations):
            if not self.handle_tick():
                return
            self.handle_reproduction()
            self.calculate_stats_per_generation()
            self.max_organisms = max(self.max_organisms, len(self.organisms))
            self.generation += 1

    def handle_tick(self):
        self.handle_predation()
        if self.check_if_over():
            return False
        self.calculate_stats_per_generation()
        return True

    def handle_predation(self):
        pass

    def check_if_over(self):
        if len(self.organisms) <= 0:
            print("organisms died out")
            return True
        return False

    def handle_reproduction(self, gene_to_mutate=None):
        organisms_to_append = []
        for organism in self.organisms:
            offspring = organism.reproduce(gene_to_mutate=gene_to_mutate)
            print(offspring)
            organisms_to_append.extend(offspring)
        self.organisms.extend(organisms_to_append)

    def calculate_stats_per_generation(self):
        self.generation_marks.append(self.generation)
        self.num_organisms.append(len(self.organisms))

    def plot_results(self):
        X = self.generation_marks
        y = self.num_organisms
        plt.plot(X, y)
        plt.fill_between(X, 0, y, facecolor='blue', alpha=.5)
        plt.xlabel('Reproductive Generation', fontsize=14)
        plt.ylabel('Number of Organisms', fontsize=14)
        plt.xticks(scipy.arange(0, self.num_generations, 5))
        plt.yticks(scipy.arange(0, self.max_organisms + 50, 25))
        plt.show()

    def add_organism(self, organism):
        self.organisms.append(deepcopy(organism))

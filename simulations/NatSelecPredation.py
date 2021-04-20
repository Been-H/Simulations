class NatSelectPredationSim(Simulation):

    def __init__(self, num_generations, max_organisms, hunting_rate):
        super().__init__(num_generations, max_organisms)
        self.hunting_rate = hunting_rate
        self.average_speeds = []

    def handle_predation(self):
        for organism in self.organisms[:]:
            speed = organism.get_trait("Speed")
            if r.random() < self.hunting_rate:
                if speed.value <= 2:
                    self.organisms.remove(organism)
                elif speed.value < 5:
                    if r.random() < .5:
                        self.organisms.remove(organism)
                elif speed.value < 6:
                    if r.random() < .4:
                        self.organisms.remove(organism)
                else:
                    if r.random() < .3:
                        self.organisms.remove(organism)

    def handle_reproduction(self):
        if len(self.organisms) * 2 >= self.max_organisms:
            return
        organisms_to_append = []
        for organism in self.organisms:
            new_organism = deepcopy(organism)
            speed = new_organism.get_trait("Speed")
            if r.random() < speed.mutation_occurence_rate:
                speed.mutate()
            organisms_to_append.append(new_organism)
        self.organisms.extend(organisms_to_append)

    def calculate_stats_per_generation(self):
        super().calculate_stats_per_generation()
        self.calculate_average_speeds()

    def calculate_average_speeds(self):
        total = 0
        for organism in self.organisms:
            total += [trait for trait in organism.traits if trait.name == 'Speed'][0].value
        average_speed = total / len(self.organisms)
        self.average_speeds.append(average_speed)

    def plot_results(self):
        fig, (plt1, plt2) = plt.subplots(2, 1)
        fig.suptitle('Data From Simulation', fontsize=20)
        plt1.plot([i for i in range(self.generations_completed)], self.average_speeds)
        plt1.set_xlabel('Reproductive Generation', fontsize=14)
        plt1.set_ylabel('Average Value of Speed Gene', fontsize=14)
        plt1.set_xticks(scipy.arange(0, self.num_generations, 50))
        plt1.set_yticks(scipy.arange(0, 14, 1))
        plt2.plot([i for i in range(self.generations_completed)], self.num_organisms)
        plt2.set_xlabel('Reproductive Generation', fontsize=14)
        plt2.set_ylabel('Number of Bunnies', fontsize=14)
        plt2.set_xticks(scipy.arange(0, self.num_generations, 100))
        plt2.set_yticks(scipy.arange(0, self.max_organisms, 100))
        plt.show()

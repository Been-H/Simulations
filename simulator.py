from copy import deepcopy
import random as r
from matplotlib import pyplot as plt
import scipy

class Simulation:

    def __init__(self, num_generations, max_organisms):
        self.num_generations = num_generations
        self.max_organisms = max_organisms
        self.generations_completed = 0
        self.organisms = []
        self.num_organisms = []

    def run(self):
        for i in range(self.num_generations):
            for organism in self.organisms:
                print(organism)
            if not self.handle_tick():
                return
            self.generations_completed += 1
            self.calculate_stats_per_generation()

    def handle_tick(self):
        self.handle_predation()
        if self.check_if_over():
            return False
        self.handle_reproduction()
        return True

    def handle_predation(self):
        pass

    def check_if_over(self):
        if len(self.organisms) <= 0:
            print("organisms died out")
            return True

    def handle_reproduction(self):
        pass

    def calculate_stats_per_generation(self):
        self.num_organisms.append(len(self.organisms))

    def plot_results(self):
        pass

    def add_organism(self, organism):
        self.organisms.append(deepcopy(organism))

class NatSelectPredationSim(Simulation):

    def __init__(self, num_generations, max_organisms, hunting_rate):
        super().__init__(num_generations, max_organisms)
        self.hunting_rate = hunting_rate
        self.average_speeds = []

    def handle_predation(self):
        print("handling predation")
        for organism in self.organisms:
            speed = organism.get_trait("Speed")
            # if r.random() < self.hunting_rate:
            print()
            print(organism)
            print("removing")
            print()
            self.organisms.remove(organism)
                # if speed.value <= 2:
                #     print("remove")
                #     self.organisms.remove(organism)
                # elif speed.value < 5:
                #     if r.random() < .9:
                #         self.organisms.remove(organism)
                # elif speed.value < 6:
                #     if r.random() < .9:
                #         self.organisms.remove(organism)
                # else:
                #     if r.random() < .9:
                #         self.organisms.remove(organism)

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
        plt2.set_xticks(scipy.arange(0, self.num_generations, 50))
        plt2.set_yticks(scipy.arange(0, self.max_organisms, 100))
        plt.show()
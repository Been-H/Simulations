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

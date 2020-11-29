import csv

class Algo:
    def __init__(self):
        self.level_company = 0
        self.position_practice = []

    def read_file(self, filename):
        with open(filename) as data:
            csv_reader = csv.reader(data, delimiter=" ")
            next(csv_reader)
            for row in csv_reader:
                self.position_practice.append(list(map(lambda x: int(x), row)))
            self.level_company = len(self.position_practice)

    def max_practice(self):
        for layer in range(self.level_company - 2, -1, -1):
            for element in range(layer + 1):
                self.find_longest_path(layer, element)
        return self.position_practice[0][0]

    def find_longest_path(self, layer, element):
        left = self.position_practice[layer + 1][element]
        right = self.position_practice[layer + 1][element + 1]
        if left > right:
            self.position_practice[layer][element] += left
        else:
            self.position_practice[layer][element] += right
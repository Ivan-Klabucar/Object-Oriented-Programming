from time import sleep
from datetime import datetime

class SlijedBrojeva:
    def __init__(self, izvor):
        self.izvor = izvor
        self.numbers = []
    
    def kreni(self, list_of_actions):
        new_num = None
        while True:
            new_num = self.izvor.get_number()
            if new_num == -1: break
            self.numbers.append(new_num)
            for action in list_of_actions:
                action(self.numbers)
            sleep(1)

class TipkovnickiIzvor:
    def get_number(self):
        return int(input('Upišite novi broj (-1 za prekid programa): '))

class DatotecniIzvor:
    def __init__(self, path_to_file):
        self.f = open(path_to_file, 'r')
    
    def get_number(self):
        new_num = int(self.f.readline().strip())
        if new_num == -1: self.f.close()
        return new_num

def write_to_file(path_to_file, numbers):
    with open(path_to_file, 'a') as f:
        f.write(', '.join([str(x) for x in numbers]) + ' ' + str(datetime.now()) +'\n')

def print_sum(numbers):
    print(f'Sum of all numbers: {sum(numbers)}')

def print_avg(numbers):
    print(f'Sum of all numbers: {sum(numbers) / len(numbers)}')

def print_median(numbers):
    sorted_nums = sorted(numbers)
    median = None
    llen = len(numbers)
    if len(numbers) % 2 == 1:
        median = int(sorted_nums[(llen - 1) // 2])
    else:
        median = (int(sorted_nums[llen // 2]) + int(sorted_nums[llen // 2 - 1])) / 2
    print(f'Median of all numbers: {median}')

print('Datotecni izvor:')
list_of_actions = [print_sum, lambda numbers: write_to_file('brojevi_output.txt', numbers)]
s = SlijedBrojeva(DatotecniIzvor('brojevi_input.txt'))
s.kreni(list_of_actions)
print()

print('Tipkovnicni izvor:')
list_of_actions = [print_median, lambda numbers: write_to_file('brojevi_output2.txt', numbers)]
s = SlijedBrojeva(TipkovnickiIzvor())
s.kreni(list_of_actions)




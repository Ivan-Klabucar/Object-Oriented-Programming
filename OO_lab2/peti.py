#PETI
from time import sleep
from datetime import datetime

class SlijedBrojeva:
    def __init__(self, izvor, list_of_actions):
        self.izvor = izvor
        self.numbers = []
        self.list_of_actions = list_of_actions
    
    def kreni(self):
        new_num = None
        while True:
            new_num = self.izvor.get_number()
            if new_num == -1: break
            self.numbers.append(new_num)
            for action in self.list_of_actions:
                action.do(self.numbers)
            sleep(1)

class SlijedBrojevaPromatrac:
    def do(self, numbers):
        pass

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

class Write_to_file(SlijedBrojevaPromatrac):
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
    
    def do(self, numbers):
        with open(self.path_to_file, 'a') as f:
            f.write(', '.join([str(x) for x in numbers]) + ' ' + str(datetime.now()) +'\n')

class Print_sum(SlijedBrojevaPromatrac):
    def do(self, numbers):
        print(f'Sum of all numbers: {sum(numbers)}')

class Print_avg(SlijedBrojevaPromatrac):
    def do(self, numbers):
        print(f'Sum of all numbers: {sum(numbers) / len(numbers)}')

class Print_median(SlijedBrojevaPromatrac):
    def do(self, numbers):
        sorted_nums = sorted(numbers)
        median = None
        llen = len(numbers)
        if len(numbers) % 2 == 1:
            median = int(sorted_nums[(llen - 1) // 2])
        else:
            median = (int(sorted_nums[llen // 2]) + int(sorted_nums[llen // 2 - 1])) / 2
        print(f'Median of all numbers: {median}')

print('Datotecni izvor:')
list_of_actions = [Print_sum(), Write_to_file('brojevi_output.txt')]
s = SlijedBrojeva(DatotecniIzvor('brojevi_input.txt'), list_of_actions)
s.kreni()
print()

print('Tipkovnicni izvor:')
list_of_actions = [Print_median(), Write_to_file('brojevi_output2.txt')]
s = SlijedBrojeva(TipkovnickiIzvor(), list_of_actions)
s.kreni()




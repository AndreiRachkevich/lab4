class Table:
    def __init__(self, weight):
        self.weight = weight


class Truck:
    tables = []

    def __init__(self, load_capacity):
        self.load_capacity = load_capacity

    def get_loaded_capacity(self):
        loaded_capacity = 0
        for x in range(len(self.tables)):
            loaded_capacity += self.tables[x].weight
        return loaded_capacity

    def add_table(self, some_table):
        if some_table.weight + self.get_loaded_capacity() <= self.load_capacity:
            self.tables.append(some_table)
            print('Добавился стол с весом', some_table.weight, 'кг')
        else:
            print('Перегрузка!!!')
            print('Стол весом ', some_table.weight, ' кг не может быть добавлен,')
            print('т.к. грузоподъемность грузового транспорта составляет', self.load_capacity, 'кг и перегрузка составляет', self.get_loaded_capacity() + some_table.weight - self.load_capacity, ' кг')


some_truck = Truck(500)
print("Грузоподъемность грузового транспорта", some_truck.load_capacity, 'кг !!!')

table_of_tables = []
n = int(input('Введите количество столов: '))
for i in range(0, n):
    print('Введите вес:', (i + 1), '-го стола из', n, 'столов')
    weight = int(input())
    table_of_tables.append(Table(weight))

for j in range(0, n):
    some_truck.add_table(table_of_tables[j])

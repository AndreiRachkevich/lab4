# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации инкапсуляции.
# Пропишите запись и считывание (get, set) инкапсулированных полей.
# Kласс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации.
# Функции-члены реализуют запись и считывание полей (проверка корректности), расчета возраста задания (необходимость в кап. ремонте).
# Создать список объектов. Вывести:
# a) список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке;

from datetime import date


class House:
    street = 'Ленина'
    address = 0
    type_of_building = None

    def __init__(self, id=0, number=0, square=0, floor=0, number_of_rooms=0):
        self.__id = id
        self.__number = number
        self.__square = square
        self.__floor = floor
        self.__number_of_rooms = number_of_rooms

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_number(self, number):
        try:
            self.__number = int(number)
        except ValueError:
            print('Неправильно указан номер квартиры')
            exit(0)

    def get_number(self):
        return self.__number

    def set_square(self, square):
        try:
            self.__square = float(square)
        except ValueError:
            print('Неправильно указана площадь')
            exit(0)

    def get_square(self):
        return self.__square

    def set_floor(self, floor):
        try:
            self.__floor = int(floor)
        except ValueError:
            print('Неправильно указан номер этажа')
            exit(0)

    def get_floor(self):
        return self.__floor

    def set_number_of_rooms(self, number_of_rooms):
        try:
            self.__number_of_rooms = int(number_of_rooms)
        except ValueError:
            print('Неправильно указано количество комнат в квартире')
            exit(0)

    def get_number_of_rooms(self):
        return self.__number_of_rooms

    table_flats_with_rooms = []

    def add_flats_with_rooms(self, flats_with_rooms):
        self.table_flats_with_rooms.append(flats_with_rooms)

        print('-------------------------------------------------------------------------------------------')
        specified_number_of_rooms = int(input('Список квартир с каким числом комнат вы бы хотели посмотреть?'))

        print('Список квартир, имеющих заданное число комнат:')
        print('-------------------------------------------------------------------------------------------')
        print('ID квартиры', ' Номер квартиры')

        for flat_with_room in flats_with_rooms:
            if flat_with_room['Число комнат'] == specified_number_of_rooms:
                print(flat_with_room['ID квартиры'], '\t\t\t', flat_with_room['Номер квартиры'])

    table_flats_on_floors = []

    def add_flats_on_floors(self, flat_on_floors):
        self.table_flats_on_floors.append(flat_on_floors)

        print('-------------------------------------------------------------------------------------------')
        print(
            'Введите  параметры список квартира, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке:')
        number_of_rooms_on_floor = int(input('Число комнат:'))
        first_floor = int(input('номер этажа с которого начинается список:'))
        last_floor = int(input('Номер этажа с которого заканвается список:'))

        print('Список квартир, имеющих', number_of_rooms_on_floor, 'комнату(ы) и расположенные на этaжах c', first_floor, 'по', last_floor)
        print('-------------------------------------------------------------------------------------------')
        print('ID квартиры', ' Номер квартиры')

        for flat_on_floor in flat_on_floors:
            if number_of_rooms_on_floor == flat_on_floor['Число комнат'] and first_floor <= flat_on_floor['Этаж'] <= last_floor:
                print(flat_on_floor['ID квартиры'], '\t\t\t', flat_on_floor['Номер квартиры'])

    @staticmethod
    def calculate_age_of_builder(service_life, age_of_building_for_repair):
        return age_of_building_for_repair - service_life

    @classmethod
    def determine_age_building(cls):
        age_house = int(input('Введите год постройки задания(дома):'))
        count_years = date.today().year - age_house
        result = cls.calculate_age_of_builder(count_years, 50)
        return result


houses = House(1, 2, 3, 4, 5)

print('Введите номер дома на улице', House.street, ': ')
House.address = int(input())

print('Введите количество квартир в доме №', House.address, ', на улице', House.street, ': ')
n = int(input())

houses.house_list = []
for i in range(0, n):
    houses.set_id(i + 1)
    id_flat = houses.get_id()

    print('Введите номер', (i + 1), 'квартиры из', n, 'квартир')
    houses.set_number(input())
    number_flat = houses.get_number()

    print('Введите площадь квартиры №', number_flat)
    houses.set_square(input())
    square_of_flat = houses.get_square()

    print('Введите этаж, где находится квартира №', number_flat)
    houses.set_floor(input())
    floor_of_flat = houses.get_floor()

    print('Введите количество комнат в квартире №', number_flat)
    houses.set_number_of_rooms(input())
    number_of_rooms_in_flat = houses.get_number_of_rooms()

    houses.house_list.append({'ID квартиры': id_flat,
                              'Номер квартиры': number_flat,
                              'Площадь квартиры': square_of_flat,
                              'Этаж': floor_of_flat,
                              'Число комнат': number_of_rooms_in_flat
                              })
    if id_flat == n:
        print('-------------------------------------------------------------------------------------------')
        age = House.determine_age_building()

        print('-------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------')

        if age > 1:
            print('До кап. ремонта дома №', House.address, ', по улице', House.street, ' осталась', age, 'лет(года)')
        elif age == 1:
            print('До кап. ремонта дома №', House.address, ', по улице', House.street, ' остался', age, 'год')
        elif age < 0:
            print('Кап. ремонт дома №', House.address, ', по улице', House.street, 'нужно уже делать')

        print('-------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------')

        print('Введите тип здания, если промышленное (p - латинская), если  гражданское (g)')
        House.type_of_building = input()

        if House.type_of_building == 'p' or House.type_of_building == 'P':
            House.type_of_building = 'промышленное'
        elif House.type_of_building == 'g' or House.type_of_building == 'G':
            House.type_of_building = 'гражданское'
        else:
            print('Нет токого типа здания')
            exit(0)

        print('-------------------------------------------------------------------------------------------')
        print('-------------------------------------------------------------------------------------------')

        print('Дом №', House.address, ', по улеце', House.street, '. Тип здания', House.type_of_building, '.')
        for flat in houses.house_list:
            print('ID квартиры', ' Номер квартиры', ' Площадь квартиры  ', ' Номер этажа  ', '  Число комнат')
            print(flat['ID квартиры'], '\t\t\t', flat['Номер квартиры'], '\t\t\t\t', flat['Площадь квартиры'],
                  '\t\t\t\t', flat['Этаж'], '\t\t\t\t', flat['Число комнат'])
            print('-------------------------------------------------------------------------------------------')
        houses.add_flats_with_rooms(houses.house_list)
        houses.add_flats_on_floors(houses.house_list)
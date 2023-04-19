class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print(f'Computations resulted in {self.__cpu * self.__memory}')

    def __str__(self):
        return (f'Computer characteritics: \n'
                f'\t\tcpu: {self.__cpu} | memory {self.__memory}')

    def __eq__(self, obj):
        return self.__memory == obj.__memory

    def __ne__(self, obj):
        return self.__memory != obj.__memory

    def __lt__(self, obj):
        return self.__memory < obj.__memory

    def __gt__(self, obj):
        return self.__memory > obj.__memory

    def __le__(self, obj):
        return self.__memory <= obj.__memory

    def __ge__(self, obj):
        return self.__memory >= obj.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} '
              f'- {self.__sim_cards_list[sim_card_number - 1]}]')

    def __str__(self):
        return f"sim_cards_list: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Проложен маршрут до "{location}"')

    def __str__(self):
        return (f'SmartPhone characteristics: \n'
                f'\t{Computer.__str__(self)}\n'
                f'\t{Phone.__str__(self)}')


macbook_pc = Computer(3.4, 1024)
nokia_phone = Phone(['Beeline', 'Mega', 'O!'])
apple_smartphone = SmartPhone(2.4, 512, ['Mega'])
samsung_smartphone = SmartPhone(1.9, 128, ['Beeline', 'O!'])

print(macbook_pc)
print(nokia_phone)
print(apple_smartphone)
print(samsung_smartphone)
print(macbook_pc == apple_smartphone)
print(macbook_pc != apple_smartphone)
print(macbook_pc < apple_smartphone)
print(macbook_pc <= apple_smartphone)
print(macbook_pc > apple_smartphone)
print(macbook_pc >= apple_smartphone)
print(samsung_smartphone == apple_smartphone)
print(samsung_smartphone != apple_smartphone)
print(samsung_smartphone < apple_smartphone)
print(samsung_smartphone <= apple_smartphone)
print(samsung_smartphone > apple_smartphone)
print(samsung_smartphone >= apple_smartphone)
macbook_pc.make_computations()
nokia_phone.call(1, '+9968005553535')
apple_smartphone.use_gps('TSUM')
apple_smartphone.call(1, '77777777')
samsung_smartphone.use_gps('OSH')
samsung_smartphone.call(2, '999999999999')
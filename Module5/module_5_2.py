class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'There is new House "{self.name}" with {self.number_of_floors} floors')

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors
        print(f'New number of "{self.name}" floors: {self.number_of_floors}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.setNewNumberOfFloors(45)
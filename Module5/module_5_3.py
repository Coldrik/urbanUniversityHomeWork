class Building():
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

h1 = Building (32, 'Big')
h2 = Building (2, 'Small')
h3 = Building (32, 'Big')

print(h1 == h2)
print(h1 == h3)

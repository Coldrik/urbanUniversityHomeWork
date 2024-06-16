class Building():

    building_total = 0
    def __init__(self, numberOfFloors, nameOfBuilding):
        self.numberOfFloors = numberOfFloors
        self.nameOfBuilding = nameOfBuilding
        Building.building_total += 1


listOfBuilding = []
for i in range(40):
    a = 'a' + str(i+1)
    listOfBuilding.append(Building(5, a))
    print('Создано здание: ', listOfBuilding[i].nameOfBuilding)
print('Количество зданий: ', Building.building_total)



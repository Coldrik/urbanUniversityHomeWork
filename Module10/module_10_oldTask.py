import multiprocessing


class WarehouseManager:
    data = {}

    def __init__(self):
        # self.data = {}
        print('Create Warehouse')



    def process_request(self, task):
        # print(task)

        if task[0] in WarehouseManager.data.keys():
            # print('task[0] in self.data.keys()')
            if task[1] == 'receipt':
                WarehouseManager.data[task[0]] += task[2]
            elif task[1] == 'shipment':
                WarehouseManager.data[task[0]] -= task[2]
            else:
                print('Нет таких команд, сэр')
        else:
            if task[1] == 'receipt':
                WarehouseManager.data[task[0]] = task[2]
            elif task[1] == 'shipment':
                WarehouseManager.data[task[0]] = task[2]
            else:
                print('Нет таких команд, сэр')
        return WarehouseManager.data

    def run(self, request):
        with multiprocessing.Pool(processes=4) as pool:
            WarehouseManager.data = pool.map(self.process_request, request)

if __name__ == '__main__':
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # manager.process_request(requests)

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(WarehouseManager.data)

import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")
import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            self.new_Runner = Runner('Forest', speed=-6)
            for _ in range(10):
                self.new_Runner.walk()
            # self.assertEqual(self.new_Runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except Exception as exc:
            # self.assertTrue(False)
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.new_Runner = Runner(None)
            for _ in range(10):
                self.new_Runner.run()
            # self.assertEqual(self.new_Runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except Exception as exc:
            # self.assertTrue(False)
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        try:
            self.new_Runner1 = Runner('Forest')
            self.new_Runner2 = Runner('Gump')
            for _ in range(10):
                self.new_Runner1.walk()
                self.new_Runner2.run()
            # self.assertNotEqual(self.new_Runner1.distance, self.new_Runner2.distance)
            logging.info('"test_challenge" выполнен успешно')
        except Exception as exc:
            # self.assertTrue(False)
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='UTF-8',
    #                     format="%(asctime)s | %(levelname)s | %(message)s")
    # unittest.main()
    t = RunnerTest()
    t.test_walk()
    t.test_run()
    t.test_challenge()

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

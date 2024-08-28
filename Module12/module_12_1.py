import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest (TestCase):

    def test_walk(self):
        self.new_Runner = Runner('Forest')
        for _ in range(10):
            self.new_Runner.walk()
        self.assertEqual(self.new_Runner.distance, 50)

    def test_run(self):
        self.new_Runner = Runner('Gump')
        for _ in range(10):
            self.new_Runner.run()
        self.assertEqual(self.new_Runner.distance, 100)

    def test_challenge(self):
        self.new_Runner1 = Runner('Forest')
        self.new_Runner2 = Runner('Gump')
        for _ in range(10):
            self.new_Runner1.walk()
            self.new_Runner2.run()
        self.assertNotEqual(self.new_Runner1.distance, self.new_Runner2.distance)

if __name__ == '__main__':
    unittest.main()
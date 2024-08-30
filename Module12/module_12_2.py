import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

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

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.sprint1 = Runner('Усэйн', speed=10)
        self.sprint2 = Runner('Андрей', speed=9)
        self.sprint3 = Runner('Ник', speed=3)
        self.round1_list = [self.sprint1, self.sprint3]
        self.round2_list = [self.sprint2, self.sprint3]
        self.round3_list = [self.sprint1, self.sprint2, self.sprint3]


    @classmethod
    def tearDownClass(cls):
        for i in range(len(cls.all_results)):
            print(cls.all_results[i])

    def test_round1(self):
        sprinters = self.round1_list
        self.r = Tournament (90, *sprinters)
        self.all_results.append(self.r.start())
        self.assertTrue(self.all_results[0][2] == sprinters[len(sprinters)-1])

    def test_round2(self):
        sprinters = self.round2_list
        self.r = Tournament (90, *sprinters)
        self.all_results.append(self.r.start())
        self.assertTrue(self.all_results[1][2] == sprinters[len(sprinters)-1])

    def test_round3(self):
        sprinters = self.round3_list
        self.r = Tournament (90, *sprinters)
        self.all_results.append(self.r.start())
        self.assertTrue(self.all_results[2][3] == sprinters[len(sprinters)-1])


if __name__ == '__main__':
    unittest.main()
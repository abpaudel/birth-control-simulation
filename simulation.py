import numpy as np

MALE_FERTILE_AT = 15*365
FEMALE_FERTILE_AT = 18*365
MALE_COPULATION_GAP = 0
FEMALE_COPULATION_GAP = 365
MALE_PROBABILITY = 0.5
LIFE_EXPECTANCY = 75*365
ZIPPERS_ZIPPED_PROB = 0.1
LEGS_CLOSED_PROB = 0.5

np.random.seed(0)

class Male():

    def __init__(self, age=1):
        self.age = age
        self.days_to_copulate = max(MALE_FERTILE_AT - self.age, 0)
        self.children = 0
        self.zippers = None
        self.update_zippers()

    def add_child(self):
        children += 1
        self.days_to_copulate = MALE_COPULATION_GAP

    def can_copulate(self):
        return (not self.zipped) and (self.days_to_copulate == 0)

    def update_age(self):
        self.age += 1
        self.update_zippers()
        self.days_to_copulate -= 1

    def update_zippers(self):
        self.zippers = bool(np.random.binomial(1, ZIPPERS_ZIPPED_PROB))


class Female():

    def __init__(self, age=1):
        self.age = age
        self.days_to_copulate = max(FEMALE_FERTILE_AT - self.age, 0)
        self.children = 0
        self.legs = None
        self.update_legs()

    def add_child(self):
        children += 1
        self.days_to_copulate = FEMALE_COPULATION_GAP

    def can_copulate(self):
        return (not self.legs_closed) and (self.days_to_copulate == 0)

    def update_age(self):
        self.age += 1
        self.update_legs()
        self.days_to_copulate -= 1

    def update_legs(self):
        self.legs = bool(np.random.binomial(1, LEGS_CLOSED_PROB))


class Population():

    def __init__(self, men=50, women=50):
        self.men = list([Male(age=MALE_FERTILE_AT) for i in range(men)])
        self.women = list([Female(age=FEMALE_FERTILE_AT) for i in range(women)])        

    def get_male(self):
        while True:
            index = np.random.randint(0, len(self.men))
            if self.men[index].can_copulate():
                return self.men[index]
            else:
                continue

    def get_female(self):
        while True:
            index = np.random.randint(0, len(self.women))
            if self.women[index].can_copulate():
                return self.women[index]
            else:
                continue

    def add_male(self, male):
        self.men.append(male)

    def add_female(self, female):
        self.women.append(female)

    def get_count(self):
        return len(self.men) + len(self.women)

    def able_men_count(self):
        return sum([1 for man in self.population.men if man.can_copulate()])

    def able_women_count(self):
       return sum([1 for woman in self.population.women if woman.can_copulate()])


class Simulator():

    def __init__(self, days=10000000, men=50, women=50):
        self.days=days
        self.population = Population(men, women)
        self.men_count = []
        self.able_men_count = []
        self.able_women_count = []

    def copulate_1_1(self, man, woman):
        man.add_child()
        woman.add_child()
        sex = np.random.binomial(1, MALE_PROBABILITY)
        return Male() if sex else Female()

    def copulate_all(self):
            while True:
                male = self.population.get_male()
                female = self.population.get_female()
                if male and female:
                    child = self.copulate_1_1(male, female)
                    if isinstance(child, Male):
                        self.population.add_male(child)
                    elif isinstance(child, Female):
                        self.population.add_female(child)
                else:
                    break

    def next_day(self):
        for man in self.population.men:
            man.update_age()
        for woman in self.population.women:
            woman.update_age()

    def simulate(self):
        for i in range(self.days):
            self.men_count.append(len(self.population.men))
            self.women_count.append(len(self.population.women))
            self.able_men_count.append(self.population.able_men_count())
            self.able_women_count.append(self.population.able_women_count())
            self.copulate_all()
            self.next_day()
            










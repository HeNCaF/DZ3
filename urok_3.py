# class Human:
#     def __init__(self, name = "Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#     def add_passengers(self, *args):
#         for passenger in args:
#             self.passengers.append(passenger)
#     def print_passengers_names(self):
#         if self.passengers != []:
#             print(f"{self.brand} has passengers: ")
#             for passengers in self.passengers:
#                 print(passengers.name)
#         else:
#             print("Car is empty")
# kate = Human("nicky")
# nick = Human("ROBERTOOOOO")
# car = Auto("Hundai")
# car.add_passengers(kate, nick)
# car.print_passengers_names()
import random
class Human:
    def __init__(self, name = "Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.work = work
        self.car = car
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car(brands_of_car)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
                self.satiety += 5
                self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
    def shopping(self.manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
            if manage == "fuel":
                print("I bought fuel")
                self.money -= 100
                self.car.fuel += 100
            elif manage == "food":
                print("I bought food")
                self.money -= 50
                self.home.food += 50
            elif manage == "delicacies":
                print("I bought delicacies")
                self.gladness += 10
                self.satiety += 2
                self.money -= 15
    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day :=^ 50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money = {self.money}")
        print(f"Satiety = {self.satiety}")
        print(f"Gladness = {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food = {self.home.food}")
        print(f"Mess = {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel = {self.car.fuel}")
        print(f"Strength = {self.car.strength}")
    def is_alive(self):
        if self.gladness < 0:
            print("Son of Miyagi")
            return False
        if self.satiety < 0:
            print("ded")
            return False
        if self.money <- 500:
            print("Loh")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_bitches()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            print(f"Salary = {self.job.job}, salary {self.job.salary}")
            self.day_indexes(day)
            dice = random.randint(1, 4):
            if self.satiety < 20:
                print("nado zhrat")
                self.eat()
            elif self.gladness < 20:
                if self.home.mess > 15:
                    print("I want to chill, but there is so")
                    self.clean_home()
                else:
                    

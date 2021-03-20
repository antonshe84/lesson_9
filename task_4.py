"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police:
            self.police_show = "(полицейская) "
        else:
            self.police_show = ""

    def go(self):
        print(f"Машина {self.name} {self.police_show}поехала!")

    def stop(self):
        print(f"Машина {self.name} {self.police_show}остановилась!")

    def turn(self, direction):
        if direction == "left":
            print(f"Машина {self.name} {self.police_show}повернула на лево!")
        elif direction == "right":
            print(f"Машина {self.name} {self.police_show}повернула на право!")
        else:
            print(f"Машина {self.name} {self.police_show}едет без поворота!")

    def show_speed(self):
        print(f"Машина {self.name} {self.police_show}едет со скоростью {self.speed}!")

    def set_speed(self, speed):
        self.speed = speed


class TownCar(Car):
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}!")
        if self.speed > 60:
            print(f"Внимание!! Превышение скорости!")


class WorkCar(Car):
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}!")
        if self.speed > 40:
            print(f"Внимание!! Превышение скорости!")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car_1 = TownCar("Lada", 50, "red")
car_1.show_speed()
car_1.set_speed(70)
car_1.show_speed()

car_2 = WorkCar("Belaz", 50, "black")
car_2.show_speed()
print(f"Цвет автомобиля {car_2.name} - {car_2.color}")

car_3 = SportCar("Bugati", 200, "green")
car_3.turn("left")
car_3.turn("right")
car_3.stop()

car_4 = PoliceCar("Toyota", 0, "blue", is_police=True)
car_4.show_speed()
car_4.go()
car_4.set_speed(100)
car_4.show_speed()
car_4.turn("left")
car_4.stop()

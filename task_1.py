"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
 — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

from time import sleep


class TrafficLight:
    def __init__(self, auto=True, color="red", time_d=10):
        if auto:
            self.svet_param = [(7, 1, 0, 0),
                               (2, 1, 3, 0),
                               (10, 0, 0, 2),
                               (2, 0, 3, 0)
                               ]
        else:
            if color == "red":
                self.svet_param = [(time_d, 1, 0, 0)]
            elif color == "yellow":
                self.svet_param = [(time_d, 0, 3, 0)]
            elif color == "green":
                self.svet_param = [(time_d, 0, 0, 2)]
            else:
                self.svet_param = [(time_d, 1, 3, 2)]

        __color = (0, 0, 0)
        __time = time_d

    def running(self):
        for i in self.svet_param:
            __time = i[0]
            __color = (i[1], i[2], i[3])
            print(f"\b" * 10, end="")
            print(f"\033[4{__color[0]}m   \033[4{__color[1]}m   \033[4{__color[2]}m   ", end="")
            sleep(__time)


if __name__ == '__main__':
    svetofor = TrafficLight()
    for _ in range(2):
        svetofor.running()

    svetofor = TrafficLight(False, "red", 10)
    svetofor.running()

    svetofor = TrafficLight(False, "green", 10)
    svetofor.running()

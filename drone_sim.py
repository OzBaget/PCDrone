from point import Point
from math import sin, cos, radians
from djitellopy import tello
from time import sleep

me = tello.Tello()


class DroneSim:
    def __init__(self, station: Point, angle):
        self.currentPos = station
        self.currentAngle = angle
        self._station = station
        me.connect()

    def is_flying(self):
        return me.is_flying()

    def takeoff(self):
        me.takeoff()

    def getBattery(self):
        return me.get_battery()

    def land(self):
        me.land()

    def go_to(self, point):
        #        self._bp.add_mark(point, 5, (0, 255, 0))
        angle = point.angle(self.currentPos) - self.currentAngle
        distance = self.currentPos.distance(point)
        self.__rotate(angle)
        self.__move(distance)

    def __rotate(self, deg):
        # print("rotating {dir} ".format(dir="right" if self.currentAngle + deg > 0 else "left") + str(
        #    int(abs(deg))) + "°....")
        self.currentAngle = (self.currentAngle + deg) % 360
        # print("Done! current angle:" + str(int(self.currentAngle)) + "°")
        me.rotate_clockwise(int(deg))

    def __move(self, cm):
        # self._bp.add_mark(self.currentPos, 3, (0, 0, 255))
        # self._bp.save(self._flightStatusFN)
        self.currentPos += Point(cos(radians(self.currentAngle)), sin(radians(self.currentAngle))) * cm
        me.move_forward(int(cm))

    def get_frame(self):
        me.streamon()
        return me.get_frame_read().frame



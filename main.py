import base64
import requests as requests
from djitellopy import tello
from time import sleep
from point import Point
from drone_sim import DroneSim
import drone_sim
import cv2

drone = drone_sim.DroneSim(Point(0, 0), 0)
print(drone.getBattery())


def recieveCommand():
    status = {
        "x": drone.currentPos.x,
        "y": drone.currentPos.y,
        "currentAngle": drone.currentAngle,
        "battery": drone.getBattery()
    }
    response = requests.post(
        'http://127.0.0.1:81/getInstructions', json=status)
    return response.text


while True:
    # streaming
    # img = drone.get_frame()
    # img = cv2.resize(img, (800, 600))
    # retval, im_bytes = cv2.imencode('.jpg', img)
    # im_b64 = (base64.b64encode(im_bytes)).decode('UTF-8')
    # print(f"\n\nlen: {len(im_b64)}\n\n")
    # data = {'framebs64': im_b64}
    # requests.post(
    #     'http://127.0.0.1:81/add-frame', json=data)

    # commands from API
    message = recieveCommand()
    comm = message.split()
    if comm[0] == "print":
        print ("I am Baget")
    elif comm[0] == "land":
        drone.land()
    elif comm[0] == "takeoff":
        drone.takeoff()
    elif comm[0] == "sleep":
        sleep(int(comm[1]))
    elif comm[0] == "go":
        drone.go_to(Point(comm[1], comm[2]))

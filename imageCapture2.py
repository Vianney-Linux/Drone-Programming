from pysimverse import Drone


drone=Drone()
angle=-360
drone.connect()
drone.set_speed(350)
drone.take_off(190)
# drone.set_rotation_speed(200)
drone.rotate(-60)
drone.move_forward(500)

while True:

    drone.rotate(angle)
    drone.rotate_camera(angle)
    drone.move_forward(300)
    if(angle-180!=-720):
        angle-=180
    else:
        angle=-270

drone.land()

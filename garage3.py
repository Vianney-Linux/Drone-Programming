from pysimverse import Drone

drone=Drone()#Create a drone object
drone.connect()#Connect the drone
drone.set_speed(200)#Set a speed of the drone object
drone.take_off(100)#Set the altitute to 1 yaw
drone.rotate(-30)#Rotate by -30
drone.move_left(45)
drone.move_forward(400)
drone.move_down(75)#Reduce the yaw by 75
drone.rotate(150)
drone.move_forward(500)
drone.move_left(75)
drone.land()#Land the drone

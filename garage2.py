from pysimverse import Drone

drone=Drone()#Instance of Drone's Class
drone.connect()#Connect to Pysimverse Simulator
drone.set_speed(200)#Set Speed
drone.take_off(100)#Set the altitute
drone.rotate_camera(-60)
drone.rotate(-60)#Rotate the drone
drone.move_left(75)#Move Left by 75 miles
drone.move_forward(250)#Reach the first Target
drone.rotate(130)
drone.move_forward(575)#Reach the two remaining targets
drone.land()#Land off the drone

from pysimverse import Drone

# Garage Level 1
drone=Drone()#Instance of a Drone's class
drone.connect()#Connect the Drone object to Pysimverse Simulator
drone.set_speed(100)#Change Speed
drone.take_off(50)#Set the yaw
drone.move_forward(220)#Move Forward upto 220miles
drone.set_rotation_speed(100)
drone.rotate(-45)#Rotate the drone
drone .rotate_camera(-45)
drone.move_forward(250)
drone.land()#Land the drone


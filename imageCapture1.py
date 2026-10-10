from pysimverse import Drone

drone=Drone()#Drone Object
drone.connect()#Connect both application
drone.take_off(150)#Land off the drone
drone.set_speed(100)#Set the speed
drone.move_forward(200)
drone.rotate(360)#Rotate by 360
print("In Pysimverse,Press the button 'z' or 'Z' to make a capture")
drone.set_rotation_speed(100)

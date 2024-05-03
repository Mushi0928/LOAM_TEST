import math
import rospy
import airsim
import numpy  as np
from geometry_msgs.msg import Point
from sensor_msgs.msg import LaserScan,PointCloud, PointCloud2, PointField

rospy.init_node("position_publisher")

pub = rospy.Publisher('rotor_position', Point, queue_size=10)
rate = rospy.Rate(1)

client = airsim.MultirotorClient()
client.confirmConnection()
#client.enableApiControl(True)
client.armDisarm(True)

while not rospy.is_shutdown():
    position = client.getMultirotorState().kinematics_estimated.position
    point = Point(x=position.x_val, y=position.y_val, z=position.z_val)

    pub.publish(point)
    rate.sleep()
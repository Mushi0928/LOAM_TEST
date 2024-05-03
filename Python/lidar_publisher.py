import math
import rospy
import airsim
import numpy  as np
from geometry_msgs.msg import Point32
from sensor_msgs.msg import LaserScan,PointCloud, PointCloud2, PointField

from geometry_msgs.msg import TransformStamped

def pub_lidar_tf():
    tf = TransformStamped()

    pass
def pub_pointcloud2(points):
    pc2 = PointCloud2()
    pc2.header.stamp = rospy.Time.now()
    pc2.header.frame_id = "velodyne"
    pc2.height = 1
    pc2.width = len(points)
    pc2.fields = [
        PointField('x', 0, PointField.FLOAT32, 1),
        PointField('y', 4, PointField.FLOAT32, 1),
        PointField('z', 8, PointField.FLOAT32, 1),
        PointField('intensity', 12, PointField.FLOAT32, 1),
        #PointField('ring', 16, PointField.UINT16, 1),
        #PointField('time', 20, PointField.FLOAT32, 1)
    ]

    pc2.is_bigendian = False
    pc2.point_step = 24
    pc2.row_step = pc2.point_step * points.shape[0]
    pc2.is_dense = True

    pc2.data = np.asarray(points, np.float32).tobytes()

    return pc2
# def pub_pointcloud(points):
# 	pc = PointCloud()
# 	pc.header.stamp = rospy.Time.now()
# 	pc.header.frame_id = 'lidar'

# 	for i in range(len(points)):
# 		pc.points.append(Point32(points[i][0],points[i][1],points[i][2]))
# 	#print('pc:',pc)
# 	return pc

def main():
    client = airsim.MultirotorClient()
    client.confirmConnection()
    #client.enableApiControl(True)
    client.armDisarm(True)
    
    pointcloud_pub = rospy.Publisher('/velodyne_points', PointCloud2, queue_size=10)
    rate = rospy.Rate(60) #original:30
	
    while not rospy.is_shutdown():
        lidarData = client.getLidarData()
        print(len(lidarData.point_cloud))
        #continue
        # a = np.zeros((2,2), dtype=int)
        # a [:, 0 ] = 1
        # print(a)
        # a[:, 0] = np.negative(a[:, 0])
        # print(a)
        # exit()
        if len(lidarData.point_cloud) > 3:
            points = np.array(lidarData.point_cloud, dtype=np.dtype('f4'))
            points = np.reshape(points, (int(points.shape[0]/3), 3))
            #print((points.shape))
            #print(points)
            points[:, [0, 1]] = points[:, [1, 0]]
            points[:, 2] = np.negative(points[:, 2])
            #print(points)
            #exit()
            num_temp = np.shape(points)[0]

            numpy_temp = np.zeros(num_temp)
            numpy_temp1 = np.ones(num_temp)
			
            points = np.c_[points, numpy_temp1, numpy_temp, numpy_temp]
            pc = pub_pointcloud2(points)
            #print(pc)
            pointcloud_pub.publish(pc)
            rate.sleep()
        else:
              print("No Lidar Data received!")

if __name__ == "__main__":
      rospy.init_node('airsim_publisher')
      main()
	# # connect the simulator
	# client = airsim.MultirotorClient()
	# client.confirmConnection()
	# client.enableApiControl(True)
	# client.armDisarm(True)
	# #rospy.init_node('airsim_publisher', anonymous=True)
	# pointcloud_pub = rospy.Publisher('/pointcloud2', PointCloud2, queue_size=100)
	# rate = rospy.Rate(30)
	
    # while
	# for i in range(5):
	# 	l = client.getLidarData()
	# 	print(len(l.point_cloud))
	# exit()
	# while not rospy.is_shutdown():

	# 	# get the lidar data
	# 	lidarData = client.getLidarData()
	# 	#print('lidar',lidarData)
	# 	print(len(lidarData.point_cloud))
		
	# 	if len(lidarData.point_cloud) >3:

	# 		points = np.array(lidarData.point_cloud,dtype=np.dtype('f4'))
	# 		points = np.reshape(points,(int(points.shape[0]/3),3))
	# 		#print('points:',points)
	# 		#pc = pub_pointcloud(points)
	# 		#pointcloud_pub.publish(pc)
	# 		#rate.sleep()
	# 		#exit()
	# 	else:
			# print("\tNo points received from Lidar data")

# if __name__ == "__main__":
# 	rospy.init_node('drone1_lidar',anonymous=True)
# 	main()

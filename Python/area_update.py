#!/usr/bin/env python
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2, PointField
import numpy as np

import threading

CUBE_SIZE = 50.0
CUBE_HALF = 25.0

pointcloud_map = {}
pointcloud_lock = threading.Lock()

def np2msg(points, frame_id): #copied code from the internet
    """
    numpy 转 msg
    Args:
        points:(numpy)
        frame_id:(str)

    Returns:(PointCloud2)
    # return pcl2.create_cloud_xyz32(header, data_process[::3])
    # return pcl2.create_cloud(header, point_fields, data_process[::3])  # 每三个点取一个
    """
    point_fields = [PointField(name='x', offset=0,
                               datatype=PointField.FLOAT32, count=1),
                    PointField(name='y', offset=4,
                               datatype=PointField.FLOAT32, count=1),
                    PointField(name='z', offset=8,
                               datatype=PointField.FLOAT32, count=1),
                    PointField(name='intensity', offset=12,
                               datatype=PointField.FLOAT32, count=1)]
    header = Header(frame_id=frame_id, stamp=rospy.Time.now())
    points_byte = points[:, 0:4].tobytes()
    # points_byte = data_process.astype(np.float32).tobytes()
    return PointCloud2(header=header,
                       height=1,
                       width=len(points),
                       is_dense=False,
                       is_bigendian=False,
                       fields=point_fields,
                       point_step=int(len(points_byte) / len(points)),
                       row_step=len(points_byte),
                       data=points_byte)


def msg2np(msg: PointCloud2, fileds=('x', 'y', 'z', 'intensity')): #copied code from the internet
    """
    激光雷达不同, msg 字节编码不同
    Args:
        msg:
        fileds_names:
    Returns: np.array, Nx3 或者 Nx4

    """

    def find_filed(filed):
        # 顺序查找
        for f in msg.fields:
            if f.name == filed:
                return f

    data_types_size = [None,
                       {'name': 'int8', 'size': 1},
                       {'name': 'uint8', 'size': 1},
                       {'name': 'int16', 'size': 2},
                       {'name': 'uint16', 'size': 2},
                       {'name': 'int32', 'size': 4},
                       {'name': 'uint32', 'size': 4},
                       {'name': 'float32', 'size': 4},
                       {'name': 'float64', 'size': 8}]

    dtypes_list = [None, np.int8, np.uint8, np.int16, np.uint16,
                   np.int32, np.uint32, np.float32, np.float64]  # PointCloud2 中有说明

    np_list = []
    for filed in fileds:
        f = find_filed(filed)

        dtype_size = data_types_size[f.datatype]['size']
        msg_total_type = msg.point_step

        item = np.frombuffer(msg.data, dtype=dtypes_list[f.datatype]).reshape(-1, int(
            msg_total_type / dtype_size))[:, int(f.offset / dtype_size)].astype(np.float32)
        np_list.append(item)

    points = np.array(np_list).T
    return points

def callback(data):
    data_list = msg2np(data)    #convert pointcloud2 to numpy array
    print(data_list[0, 0:3])

    #seperate the data to different groups by their x,y coordinate
    temp_pointcloud = {}
    for point in data_list:
        cube_index = (int(point[0]/CUBE_SIZE), int(point[1]/CUBE_SIZE))
        if cube_index not in temp_pointcloud.keys():
            temp_pointcloud[cube_index] = []

        temp_pointcloud[cube_index].append(point)
    
    #update the stored map
    pointcloud_lock.acquire()   #multithreading lock
    for key in temp_pointcloud:
        print(len(temp_pointcloud[key]))

        #if 1. the area don't have any data
        #or 2. new data of the area have more points then the stored data
        #=> update the stored data
        if key not in pointcloud_map.keys():
            pointcloud_map[key] = temp_pointcloud[key]
        elif len(temp_pointcloud[key]) >= len(pointcloud_map[key]):
            pointcloud_map[key] = temp_pointcloud[key]
        
            
    pointcloud_lock.release()   #multithreading lock


def talker():
    #publish the stored pointcloud to ROS
    pub = rospy.Publisher('complete_map', PointCloud2, queue_size=10)
    rate = rospy.Rate(0.1) # 10hz
    while not rospy.is_shutdown():
        points = []
        
        pointcloud_lock.acquire()
        for cube_index in pointcloud_map:
            points += pointcloud_map[cube_index]
        pointcloud_lock.release()

        if len(np.shape(points)) == 2:     
            pc2 = np2msg(np.array(points), "camera_init")
            pub.publish(pc2)
            print("talked")

        rate.sleep()

def listener():
    #call the callback function when received message from LOAM
    rospy.Subscriber("laser_cloud_surround", PointCloud2, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        #talker()
        rospy.init_node('complete_map')

        talker_thread = threading.Thread(target=talker)
        
        talker_thread.start()
        listener()

        talker_thread.join()
    except rospy.ROSInterruptException:
        pass
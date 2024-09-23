#!/usr/bin/env python3


import rospy
from std_msgs.msg import Int16

def number_publisher():
    pub = rospy.Publisher('num_print', Int16, queue_size=10)
    rospy.init_node('int_publisher')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy_num= 20
        pub.publish(rospy_num)
        rate.sleep()

if __name__ == '__main__':
    try:
        number_publisher()
    except rospy.ROSInterruptException:
        pass
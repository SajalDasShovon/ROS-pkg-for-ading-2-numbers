#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def num_callback(data):
    number=data.data
    number = number +10
    print (number)
    
def number_subscriber():
    rospy.init_node('int_subscriber', anonymous=True)

    rospy.Subscriber("num_print", Int16, num_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
     number_subscriber()
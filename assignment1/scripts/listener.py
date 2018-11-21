#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

def callback(data):
    my_guess = random.randint(1,5)
    num1= data.data
    rospy.loginfo("my numner %d",num1)
    if(my_guess == num1):
        rospy.loginfo('Yaaa ... You got it')
    else:
        rospy.loginfo("You loss")

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('Guess', Int32, callback)

    # rospy.Subscriber('position', Int32, callback1)
    rospy.spin()

if __name__ == '__main__':
    listener()

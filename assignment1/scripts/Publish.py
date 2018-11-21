#!/usr/bin/env python

import random
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

def talker():
    # pub = rospy.Publisher('chatter', String, queue_size=10)
    pub = rospy.Publisher('Guess', Int32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        # hello_str = "Hi Robot guess this %s" % rospy.get_time()
        num = random.randint(1,5)
        rospy.loginfo("My Number is: %d", num)
        # pub.publish(hello_str)
        pub.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

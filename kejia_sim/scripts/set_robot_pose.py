#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from gazebo_msgs.msg import ModelState


pub=rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)

#from nav_msgs.msg import Odometry


def mcs_pose_callback(data):
    msg = ModelState()
    msg.model_name = 'kejia'
    msg.pose.position.x = data.pose.position.x
    msg.pose.position.y = data.pose.position.y
    msg.pose.orientation.w = data.pose.orientation.w
    msg.pose.orientation.x = data.pose.orientation.x
    msg.pose.orientation.y = data.pose.orientation.y
    msg.pose.orientation.z = data.pose.orientation.z
    pub.publish(msg)


if __name__ == '__main__':
    rospy.init_node('mcs_pose', anonymous=True)
    rospy.loginfo("start OK!")
    rospy.Subscriber("mcs_pose", PoseStamped, mcs_pose_callback, None, None, 65536, True)
    #rospy.Subscriber("odom", Odometry, odom_callback, None, None, 65536, True)
    rospy.spin()
import rospy
from gazebo_msgs.msg import ModelState


rospy.init_node('hello')

pub=rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=10)
msg = ModelState()
msg.model_name = 'kejia'

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    msg.pose.position.x += 0.003
    pub.publish(msg)
    rate.sleep()

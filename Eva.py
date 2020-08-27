import rospy
from std_msgs.msg import String,Int8


def callback_str(data):
    rospy.loginfo(data.data)

def callback_int(data):
    rospy.loginfo(str(data.data))

def Eva_listener():
    rospy.init_node('Eva', anonymous=False)
    rospy.Subscriber('hello',String,callback_str)
    rospy.Subscriber('hello_int',Int8,callback_int)
    rospy.spin()

if __name__ == '__main__':
    Eva_listener()

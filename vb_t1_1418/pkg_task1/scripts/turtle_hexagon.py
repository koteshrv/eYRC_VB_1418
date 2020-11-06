#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PI = 3.1415926535897

def main():

	# Make the script a ROS Node.
	rospy.init_node('node_turtle_revolving', anonymous=True)

	# Create a publisher to publish messages to a topic.
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	# Linear velocities of all the 3 axes
	vel_msg.linear.x = 0.5
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0

	# Angular velocities of all the 3 axes
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0		
	vel_msg.angular.z = 0


	# Subscribe to the topic /turtle1/pose
	rospy.Subscriber("/turtle1/pose", Pose)

	linear_vel = vel_msg.linear.x
	distance = 3
	speed = 15 # degrees/second
	angle = 60
	angular_speed = speed*2*PI/360
	relative_angle = angle*2*PI/360


	for i in range(6):
		current_distance = 0
		t0 = rospy.Time.now().to_sec()
		vel_msg.linear.x = 0.5
		vel_msg.angular.z = 0
		while(current_distance < distance):
			#rospy.loginfo("Moving straight" + str(current_distance))
			velocity_publisher.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			current_distance = linear_vel * (t1-t0)



		t2 = rospy.Time.now().to_sec()
		current_angle = 0
		vel_msg.linear.x = 0
		vel_msg.angular.z = abs(angular_speed)

		while(current_angle < relative_angle):
			velocity_publisher.publish(vel_msg)
			t3 = rospy.Time.now().to_sec()
			current_angle = angular_speed*(t3-t2)
			#rospy.loginfo("Rotated " + str(current_angle) + "  " +  str(relative_angle))

	    #Forcing our robot to stop
		vel_msg.angular.z = 0
		vel_msg.linear.x = 0
		velocity_publisher.publish(vel_msg)

	#rospy.spin()
	


		
if __name__ == '__main__':	
    try:
        main()
    except rospy.ROSInterruptException: pass







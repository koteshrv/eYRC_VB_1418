#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def main():

	# Make the script a ROS Node.
	rospy.init_node('node_turtle_revolving', anonymous=True)

	# Create a publisher to publish messages to a topic.
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	# Linear velocities of all the 3 axes
	vel_msg.linear.x = 1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0

	# Angular velocities of all the 3 axes
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0		
	vel_msg.angular.z = 1


	# Subscribe to the topic /turtle1/pose
	rospy.Subscriber("/turtle1/pose", Pose)

	# Set the Loop Rate 
	var_loop_rate = rospy.Rate(3) # 3 Hz : Loop will its best to run 3 time in 1 second

	# Takes initial time to velocity calculus
	t0 = rospy.Time.now().to_sec()

	current_distance = 0
	linear_vel = vel_msg.linear.x

	# linear_vel = radius * angular_vel 
	radius = 1	# Since angular_vel is 1
	distance = 2 * math.pi * radius 
	
	
	print("Move")

	#Loop to rotate the turtle untill it reaches the initial point
	while(current_distance < distance):

	    # Publish the velocity
	    velocity_publisher.publish(vel_msg)

	    # Takes actual time to velocity calculus
	    t1 = rospy.Time.now().to_sec()

	    # Calculates distancePoseStamped
	    current_distance= linear_vel * (t1-t0)

	    # Print info on console.
	    rospy.loginfo("Moving in a circle")

	    print(current_distance)

	    var_loop_rate.sleep()
	
	rospy.loginfo("Goal reached")

	#After the loop, stops the robot
	vel_msg.linear.x = 0

	#Force the robot to stop
	velocity_publisher.publish(vel_msg)

	var_loop_rate.sleep()
	
	# Keep the node alive till it is killed by the user.
	rospy.spin()
	


		
if __name__ == '__main__':	
    try:
        main()
    except rospy.ROSInterruptException: pass






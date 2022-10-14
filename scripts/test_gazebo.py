#!/usr/bin/env python3

# Python 2/3 compatibility imports
from __future__ import print_function
from multiprocessing.connection import wait
from six.moves import input
import commons

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("hc10_move_group_cartesian_path", anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

group_name = "hc10_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
move_group.set_goal_tolerance(0.1)
move_group.set_goal_joint_tolerance(0.1)

RIGHT_LOOKING_LEFT = Pose(position = Point(x = 0.71, y = -0.24, z = 0.17), orientation = Quaternion(x = -0.534, y = 0.503, z = -0.433, w = 0.524))
LEFT_LOOKING_RIGHT = Pose(position = Point(x = 0.71, y = 0.24, z = 0.17), orientation = Quaternion(x = -0.534, y = 0.503, z =  0.433, w = -0.524))
TOP_LOOKING_DOWN = Pose(position = Point(x = 0.65, y = 0.17, z = 1.0), orientation = Quaternion(x = 1.0, y = 0.0, z = 0.0, w = 0.0))

rospy.sleep(1)

print("Starting trajectory")

# Initialization process
print("=== Initialization process ===")
# Get back to home pose
print("> Going to 'home' pose ...", end ="", flush = True)
commons.plan_and_go(move_group, pose = commons.HOME)
print("\r> Going to 'home' pose DONE")

print("")

# Test sequence
print("=== Test sequence ===")
print("  < scanning box >")
commons.test_movement(move_group, pose = TOP_LOOKING_DOWN, pose_name = "top looking down")
commons.test_movement(move_group, pose = RIGHT_LOOKING_LEFT, pose_name = "right looking left")
commons.test_movement(move_group, pose = LEFT_LOOKING_RIGHT, pose_name = "left looking right")


print("...")
rospy.sleep(3)
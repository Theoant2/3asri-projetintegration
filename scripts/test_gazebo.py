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
print("  < trajectory without box >")
commons.test_movement(move_group, pose = commons.END, pose_name = "end")
commons.test_movement(move_group, pose = commons.HOME, pose_name = "home")

print("...")
rospy.sleep(3)
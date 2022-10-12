#!/usr/bin/env python3

# Python 2/3 compatibility imports
from __future__ import print_function
from multiprocessing.connection import wait

import sys
import copy
import rospy
import moveit_commander


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("hc10_move_group_cartesian_path", anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()

object_names = scene.get_known_object_names()

rospy.sleep(1)

for object_name in object_names:
    print(f"Removing object '{object_name}'")
    scene.remove_world_object(name = object_name)

print(f"Done")
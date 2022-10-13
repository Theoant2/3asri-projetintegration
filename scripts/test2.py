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
# Remove all objects in scene
object_names = scene.get_known_object_names()
for object_name in object_names:
    print(f"Removing object '{object_name}'")
    scene.remove_world_object(name = object_name)
if len(object_names) == 0:
    print("> Nothing to delete in the scene")
# Get back to home pose
print("> Going to 'home' pose ...", end ="", flush = True)
commons.plan_and_go(move_group, pose = commons.HOME)
print("\r> Going to 'home' pose DONE")

# Spawn table
commons.print_message("> Spawning fake table: ", "In progress ...")
is_table_spawned = commons.add_box(scene, robot, position = (0, 0, -0.05), name = "fake_table", size = (2, 2, 0.10))
commons.print_message("> Spawning fake table: ", "SUCCESS" if is_table_spawned else "TIMEOUT", padding = 11, breakline = True)

commons.print_message("> Spawning back wall: ", "In progress ...")
is_back_wall_spawned = commons.add_box(scene, robot, position = (-0.73, 0, 0.43), name = "back_wall", size = (0.10, 2, 1))
commons.print_message("> Spawning back wall: ", "SUCCESS" if is_back_wall_spawned else "TIMEOUT", padding = 11, breakline = True)

commons.print_message("> Spawning left wall: ", "In progress ...")
is_left_wall_spawned = commons.add_box(scene, robot, position = (0, 0.69, 0.43), name = "left_wall", size = (2, 0.10, 1))
commons.print_message("> Spawning left wall: ", "SUCCESS" if is_left_wall_spawned else "TIMEOUT", padding = 11, breakline = True)

commons.print_message("> Spawning left wall: ", "In progress ...")
is_right_wall_spawned = commons.add_box(scene, robot, position = (0, -0.69, 0.43), name = "right_wall", size = (2, 0.10, 1))
commons.print_message("> Spawning left wall: ", "SUCCESS" if is_right_wall_spawned else "TIMEOUT", padding = 11, breakline = True)

print("")

# Test sequence
print("=== Test sequence ===")
print("  < trajectory without box >")
commons.test_movement(move_group, pose = commons.END, pose_name = "end")
commons.test_movement(move_group, pose = commons.HOME, pose_name = "home")

box_location = (0.5, 0, 1)
box_name = "box"
print("")
print(f"> Adding a box to the scene at {box_location} with name '{box_name}' in frame '{robot.get_planning_frame()}'")
is_box_spawned = commons.add_box(scene, robot, position = box_location, name = box_name)
print(f"> Box spawning: " + ("SUCCESS" if is_box_spawned else "TIMEOUT"))
print("")
print("  < trajectory with box >")
rospy.sleep(1)

commons.test_movement(move_group, pose = commons.END, pose_name = "end")
commons.test_movement(move_group, pose = commons.HOME, pose_name = "home")


print("...")
rospy.sleep(3)
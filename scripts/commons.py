import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped

HOME = Pose(position = Point(x = 0, y = 0.162, z = 1.605), orientation = Quaternion(x = 0, y = 0, z = 1.0, w= 0))
END = Pose(position = Point(x = 0.830, y = 0.162, z = 0.888), orientation = Quaternion(x = 0, y = 0, z = 1.0, w= 0))

def compute_cartesian_path(move_group, waypoints = [], scale = 1.0):

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0,
    # ignoring the check for infeasible jumps in joint space, which is sufficient
    # for this tutorial.
    (plan, fraction) = move_group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
    )  # jump_threshold

    # Note: We are just planning, not asking move_group to actually move the robot yet:
    return plan, fraction

def plan_and_go(move_group, pose, debug = False):
    if debug:
        print(f"Planning movement to goal {pose.position}")
    move_group.set_pose_target(pose)
    if debug:
        print(f"Start movement")
    success = move_group.go(wait=True)
    if debug:
        print(f"Trajectory success: {success}")
    move_group.stop()
    move_group.clear_pose_targets()
    return success


def add_box(scene, robot, position = (0, 0, 0), rotation = (0, 0, 0, 1.0), name = "box", size = (0.2, 0.2, 0.2), removeOld = True):
    box_pose = PoseStamped()
    box_pose.header.frame_id = robot.get_planning_frame()
    box_pose.pose.orientation.x = rotation[0]
    box_pose.pose.orientation.y = rotation[1]
    box_pose.pose.orientation.z = rotation[2]
    box_pose.pose.orientation.w = rotation[3]
    box_pose.pose.position.x = position[0]
    box_pose.pose.position.y = position[1]
    box_pose.pose.position.z = position[2]
    box_name = name

    if removeOld:
        scene.remove_world_object(name = name)

    scene.add_box(box_name, box_pose, size=size)
    return wait_object_spawn(scene, object_name = box_name, timeout = 3)

def wait_object_spawn(scene, object_name, timeout = 3):
    start = rospy.get_time()
    seconds = rospy.get_time()
    while (seconds - start < timeout) and not rospy.is_shutdown():
        # Test if the box is in the scene.
        # Note that attaching the box will remove it from known_objects
        is_known = object_name in scene.get_known_object_names()

        # Test if we are in the expected state
        if (is_known):
            return True

        # Sleep so that we give other threads time on the processor
        rospy.sleep(0.1)
        seconds = rospy.get_time()

    # If we exited the while loop without returning then we timed out
    return False

def get_message(prefix, state, padding = 0):
    return "\r" + prefix + state + (" " * padding)

def print_message(prefix, state, padding = 0, breakline = False):
    print(get_message(prefix, state, padding = padding), end = "\n" if breakline else "", flush = True)

def test_movement(move_group, pose, pose_name):
    prefix = f"Going to '{pose_name}' pose: "
    print_message(prefix, "In progress ...")
    success = plan_and_go(move_group, pose = pose)
    state = ("DONE" if success else "FAILURE")
    print_message(prefix, state, padding = 11, breakline = True)
    if not success:
        print("Can not continue test sequence. Program exit")
        sys.exit(1)

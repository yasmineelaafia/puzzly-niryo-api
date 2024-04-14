from pyniryo import *

# - Constants
workspace_name = "Puzzle"  # Robot's Workspace Name
robot_ip_address = "192.168.236.141"

# The pose from where the image processing happens
observation_pose = PoseObject(
    x=0.16, y=0.0, z=0.35,
    roll=0.0, pitch=1.57, yaw=0.0,
)
# Place pose
place_pose = PoseObject(
    x=0.0, y=-0.2, z=0.12,
    roll=0.0, pitch=1.57, yaw=-1.57
)

# - Initialization

# Connect to robot
robot = NiryoRobot(robot_ip_address)
# Calibrate robot if robot needs calibration
robot.arm.calibrate_auto()
# Updating tool
robot.tool.update_tool()

robot.move_pose(observation_pose)
# Trying to pick target using camera
obj_found, shape_ret, color_ret = robot.vision.vision_pick(workspace_name)
if obj_found:
    robot.pick_place.place_from_pose(place_pose)

robot.arm.set_learning_mode(True)

robot.end()
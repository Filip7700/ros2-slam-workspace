import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro

PACKAGE_NAME = "csicsko_mk2"


def generate_launch_description():
    # Check if we have told to use sim time
    use_sim_time = LaunchConfiguration("use_sim_time")

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory(PACKAGE_NAME))
    xacro_file = os.path.join(pkg_path, "description", "robot.urdf.xacro")

    robot_description_config = xacro.process_file("/home/filip/FilipLNX/Programi/ROS2/ROS2Iron/src/gg_packs/csicsko_mk2/description/robot.urdf.xarco")

    # Create a robot_state_publisher node
    params = {
        "robot_description": robot_description_config.toxml(),
        "use_sim_time": use_sim_time}

    node_robot_state_publisher = Node(
        package = "robot_state_publisher",
        executable = "robot_state_publisher",
        output = "screen",
        parameters = [params])

    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_time",
            default_value = "false",
            description = "Use sim time if true"),
        node_robot_state_publisher])

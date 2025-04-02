import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import GroupAction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import PushRosNamespace

def generate_launch_description():
  launch_dir = os.path.join(get_package_share_directory('launch_tutorial', 'launch'))
  turtlesim_world_1 = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([launch_dir, 'turtlesim_world_1.launch.py'])
  )
  turtlesim_world_2 = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([launch_dir, 'turtlesim_world_2.launch.py'])
  )
  turtlesim_world_2_with_namesapce = GroupAction(
    actions=[
      PushRosNamespace('turtlesim2'),
      turtlesim_world_2,
    ]
  )
  
  broadcaster_listener_nodes = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([launch_dir, 'turtlesim_world_2.launch.py']),
    launch_arguments={'target_frame': 'carrot1'}.items(),
  )
  mimic_nodes = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([launch_dir, 'mimic.launch.py'])
  )
  fixed_frame_node = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([launch_dir, 'fixed_broadcaster.launch.py'])
  )
  rviz_node = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([launch_dir, 'turtlesim_rviz.launch.py'])
  )
  
  return LaunchDescription([
    turtlesim_world_1,
    turtlesim_world_2_with_namesapce,
    broadcaster_listener_nodes,
    mimic_nodes,
    fixed_frame_node,
    rviz_node,
  ])
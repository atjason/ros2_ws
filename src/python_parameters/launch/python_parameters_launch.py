from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  return LaunchDescription([
    Node(
      package='python_parameters',
      executable='minimal_node',
      name='custom_minimal_node',
      output='screen',
      emulate_tty=True,
      parameters=[
        {'my_parameter': 'earth'},
      ]
    )
  ])

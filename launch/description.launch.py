from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    enable_control = LaunchConfiguration('enable_control')
    xacro_file = PathJoinSubstitution(
        [FindPackageShare('jimmbot_description'), 'urdf', 'jimmbot.xacro']
    )
    robot_description = ParameterValue(
        Command([
            FindExecutable(name='xacro'),
            ' ',
            xacro_file,
            ' ',
            'enable_control:=',
            enable_control,
        ]),
        value_type=str,
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation clock if true.',
        ),
        DeclareLaunchArgument(
            'enable_control',
            default_value='true',
            description='Include gz_ros2_control plugin configuration in the robot description.',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {
                    'robot_description': robot_description,
                    'use_sim_time': use_sim_time,
                }
            ],
        ),
    ])
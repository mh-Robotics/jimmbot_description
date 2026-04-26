from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    gz_control_params_file = LaunchConfiguration('gz_control_params_file')
    xacro_file = PathJoinSubstitution(
        [FindPackageShare('jimmbot_description'), 'urdf', 'jimmbot.xacro']
    )
    robot_description = ParameterValue(
        Command([
            FindExecutable(name='xacro'),
            ' ',
            xacro_file,
            ' ',
            'gz_control_params_file:=',
            gz_control_params_file,
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
            'gz_control_params_file',
            default_value='gz_control.yaml',
            description='Absolute path to gz_control controller parameters YAML.',
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
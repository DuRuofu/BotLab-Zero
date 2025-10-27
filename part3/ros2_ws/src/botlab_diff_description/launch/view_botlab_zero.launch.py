from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os
import xacro

def generate_launch_description():
    pkg_path = get_package_share_directory('botlab_diff_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'botlab_zero', 'botlab_zero.urdf.xacro')

    # 生成 robot_description
    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # 启动 Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        )
    )

    # robot_state_publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}],
        output='screen'
    )

    # 延迟 spawn_entity，确保 Gazebo Ros Factory 已启动
    spawn_entity = TimerAction(
        period=3.0,  # 延迟 3 秒
        actions=[Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'botlab_zero', '-topic', 'robot_description'],
            output='screen'
        )]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_entity
    ])

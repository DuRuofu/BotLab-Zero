import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    pkg_path = get_package_share_directory('botlab_diff_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'diff_drive_car.urdf.xacro')
    world_file = os.path.join(pkg_path, 'world', 'room.world')  # 自定义世界文件路径

    # 转换 xacro 为 URDF
    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # 启动 Gazebo，加载自定义世界
    gazebo_launch = ExecuteProcess(
        cmd=['gazebo', '--verbose', world_file, '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    # robot_state_publisher 发布 TF
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True, 'robot_description': robot_desc}]
    )

    # Gazebo spawn 模型，延时 5 秒执行
    spawn_node = TimerAction(
        period=5.0,
        actions=[Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'diff_drive_car'],
            output='screen'
        )]
    )

    return LaunchDescription([
        gazebo_launch,
        rsp_node,
        spawn_node
    ])

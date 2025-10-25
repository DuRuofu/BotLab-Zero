import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    pkg_path = get_package_share_directory('botlab_diff_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'diff_drive_car.urdf.xacro')
    rviz_config_file = os.path.join(pkg_path, 'rviz', 'config.rviz') 

    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # joint_state_publisher 节点
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    # robot_state_publisher 节点
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True, 'robot_description': robot_desc}],
    )

    # rviz2 节点，加载配置文件
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file]  
    )

    return LaunchDescription([
        joint_state_publisher_node, 
        robot_state_publisher_node,
        rviz_node
    ])

import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    # 获取功能包路径
    pkg_path = get_package_share_directory('botlab_diff_description')
    xacro_file = os.path.join(pkg_path, 'urdf', 'diff_drive_car.urdf.xacro')

    # 使用 xacro 生成 urdf 内容
    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # 启动 robot_state_publisher
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True, 'robot_description': robot_desc}],
    )

    # 启动 RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([rsp_node, rviz_node])

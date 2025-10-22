# ROS2与仿真环境搭建

## 一、简介

本章节将介绍如何搭建ROS2开发环境和Gazebo仿真环境。关于搭建开发环境可以看这篇博客：[Ubuntu_22_04_ROS2安装](../../01.环境搭建/ROS2/Ubuntu_22_04_ROS2安装.md)

本次项目我们依旧使用 Ubuntu22.04 和对应的ROS2 - Humble Hawksbill

![562](attachments/Pasted%20image%2020251019115354.png)
## 二、准备虚拟机环境

首先我们需要一台安装了 Ubuntu22.04 的虚拟机，或者是使用Windows上的WSL也OK。在这个教程里，使用Windows11下的WSL2来创建Ubuntu22.04虚拟环境。至于具体的虚拟机怎么安装，WSL2怎么安装，这里不再详细说明，网上都有很多很好的教程。

在前期的仿真阶段我们先使用WSL或者虚拟机即可，这里我准备了一台 Ubuntu22.04 的WSL2虚拟机，名字叫Ubuntu-22.04-BotLab-Zero，如下图：

![](attachments/Pasted%20image%2020251019120001.png)

## 三、安装ROS2

在Linux终端里使用鱼香ROS的一键安装脚本：

```bash
wget http://fishros.com/install -O fishros && bash fishros
```



选择安装ROS:

![](attachments/Pasted%20image%2020251019121231.png)

安装humble(ROS2)桌面版：

![](attachments/Pasted%20image%2020251019121553.png)

中途不报错，安装完成如下：

![](attachments/Pasted%20image%2020251019122759.png)

使用命令`source ~/.bashrc`重新加载环境，使用`ros2`命令检验安装成功：

![](attachments/Pasted%20image%2020251019122832.png)

## 四、测试ROS环境


在终端中运行以下命令启动小海龟节点：

```bash
ros2 run turtlesim turtlesim_node
```

弹出下面的界面：

![](attachments/Pasted%20image%2020251019122952.png)


再启动一个新的终端，启动键盘控制节点：

![](attachments/Pasted%20image%2020251019124109.png)

> 在WSL环境下，可能会出现无法使用键盘控制节点去控制海龟的情况，这应该是某种bug，可以通过打开rqt 软件刷新node graph就能正常控制了。

在rqt里刷新node graph：

![](attachments/Pasted%20image%2020251019124317.png)

重新尝试控制：

![](attachments/Pasted%20image%2020251019124358.png)

到此为止我们就完成了环境的安装，至于后续要使用的其他仿真模块，比如Gazebo仿真器，我们后续使用到的时候在进行安装。
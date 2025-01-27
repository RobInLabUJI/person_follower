# Person-following Python ROS 2 template

We assume that [ROS 2](https://docs.ros.org/) and [Webots](https://cyberbotics.com/) are installed in the system. 

For the steps below we use ROS2 Humble and Webots R2023b.

1.a. Install the prerequisites
```
sudo apt install ros-humble-webots-ros2-turtlebot
```
1.b. Fix [this issue](https://github.com/cyberbotics/webots_ros2/issues/1015)
```
wget -O /tmp/hotfix.deb  http://snapshots.ros.org/humble/2024-08-28/ubuntu/pool/main/r/ros-humble-hardware-interface/ros-humble-hardware-interface_2.43.0-1jammy.20240823.145349_amd64.deb  && \
sudo apt install -y --allow-downgrades /tmp/hotfix.deb && \
rm -f /tmp/hotfix.deb
```
2. Create a ROS 2 workspace
```
mkdir -p ~/ros2_ws/src
```
3. Clone this repository and build the package
```
cd ~/ros2_ws/src
git clone https://github.com/RobInLabUJI/person_follower.git
cd ..
source /opt/ros/humble/setup.bash
colcon build --symlink-install
```
4. Copy the Webots world file to the ROS package folder
```
sudo cp ~/ros2_ws/src/person_follower/webots/*.wbt \
        /opt/ros/humble/share/webots_ros2_turtlebot/worlds/.
```
5. Run the person-following node
```
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
export ROS_LOCALHOST_ONLY=1
ros2 run person_follower person_follower 
```
6. In a new terminal, launch the Webots simulator

In a room with walls:
```
export WEBOTS_HOME=~/webots-R2023b
source /opt/ros/humble/setup.bash
export ROS_LOCALHOST_ONLY=1
ros2 launch webots_ros2_turtlebot robot_launch.py \
  world:=turtlebot3_burger_pedestrian_simple.wbt
```

Or a room without walls:
```
export WEBOTS_HOME=~/webots-R2023b
source /opt/ros/humble/setup.bash
export ROS_LOCALHOST_ONLY=1
ros2 launch webots_ros2_turtlebot robot_launch.py \
  world:=turtlebot3_burger_pedestrian_no_walls.wbt
```

7. In a new terminal, launch RViz
```
source /opt/ros/humble/setup.bash
export ROS_LOCALHOST_ONLY=1
rviz2 -d ~/ros2_ws/src/person_follower/webots/config.rviz
```

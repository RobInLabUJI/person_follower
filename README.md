# Person-following Python ROS 2 template

We assume that [ROS 2](https://docs.ros.org/) and [Webots](https://cyberbotics.com/) are installed in the system. 

For the steps below we use [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/index.html) and [Webots R2025a](https://github.com/cyberbotics/webots/releases/tag/R2025a).

We assume that Webots has been installed from [the tar.bz2 archive](https://github.com/cyberbotics/webots/releases/download/R2025a/webots-R2025a-x86-64.tar.bz2) in the folder `$HOME/webots-R2025a`. Should it be installed differently, please update the environment variable `WEBOTS_HOME` in the below instructions.

1. Install the prerequisites
```
sudo apt update
sudo apt install ros-jazzy-webots-ros2-turtlebot
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
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
```
4. Copy the Webots world file to the ROS package folder
```
sudo cp ~/ros2_ws/src/person_follower/webots/*.wbt \
        /opt/ros/jazzy/share/webots_ros2_turtlebot/worlds/.
```
5. Run the person-following node
```
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
ros2 run person_follower person_follower 
```
6. In a new terminal, launch the Webots simulator

In a room with walls:
```
export WEBOTS_HOME=~/webots-R2025a
source /opt/ros/jazzy/setup.bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
ros2 launch webots_ros2_turtlebot robot_launch.py \
  world:=turtlebot3_burger_pedestrian_simple.wbt
```

Or a room without walls:
```
export WEBOTS_HOME=~/webots-R2025a
source /opt/ros/jazzy/setup.bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
ros2 launch webots_ros2_turtlebot robot_launch.py \
  world:=turtlebot3_burger_pedestrian_no_walls.wbt
```

7. In a new terminal, launch RViz
```
source /opt/ros/jazzy/setup.bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
rviz2 -d ~/ros2_ws/src/person_follower/webots/config.rviz
```

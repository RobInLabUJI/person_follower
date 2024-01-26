# Person-following Python ROS 2 template

We assume that [ROS 2](https://docs.ros.org/) and [Webots](https://cyberbotics.com/) are installed in the system. 

For the steps below we use ROS2 Foxy and Webots R2022b.

1. Install the prerequisites
```
sudo apt install webots_ros2_turtlebot
```
2. Create a ROS 2 workspace
```
mkdir -p ros2_ws/src
```
3. Clone this repository and build the package
```
cd ros2_ws/src
git clone https://github.com/RobInLabUJI/person_follower.git
cd ..
source /opt/ros/foxy/setup.bash
colcon build --symlink-install
```
4. Copy the Webots world file to the ROS package folder
```
sudo cp webots/turtlebot3_burger_pedestrian_simple.wbt /opt/ros/foxy/share/webots_ros2_turtlebot/worlds/.
```
5. Launch the Webots simulator
```
export WEBOTS_HOME=...
source /opt/ros/foxy/setup.bash
ros2 launch webots_ros2_turtlebot robot_launch.py \
  world:=turtlebot3_burger_pedestrian_simple.wbt
```
6. Launch RViz
```
source /opt/ros/foxy/setup.bash
rviz2 -d webots/config.rviz
```
7. Run the person-following node
```
source /opt/ros/foxy/setup.bash
source install/setup.bash
ros2 run person_follower person_follower 
```

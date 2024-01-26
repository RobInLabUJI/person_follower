#!/bin/bash

export WEBOTS_HOME=$HOME/webots_R2023a
source /opt/ros/foxy/setup.bash

ros2 launch webots_ros2_turtlebot robot_launch.py \
  world:=turtlebot3_burger_pedestrian_simple.wbt

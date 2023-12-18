# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

class PersonFollower(Node):

    def __init__(self):
        super().__init__('person_follower')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, input_msg):
        self.get_logger().info("I heard a scan")
        output_msg = String()
        output_msg.data = 'Hello World'
        self.publisher_.publish(output_msg)
        self.get_logger().info('Publishing: "%s"' % output_msg.data)

def main(args=None):
    rclpy.init(args=args)

    person_follower = PersonFollower()

    rclpy.spin(person_follower)

    person_follower.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

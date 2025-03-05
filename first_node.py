#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyFirstNode(Node):
    def __init__(self):
        super().__init__('first_node')
        self.counter_=0
        self.create_timer(1.0,self.timer_callback)
        
    def timer__callback(self):
        self.get_logger().info("heloo "+ str(self.counter))
        self.counter_ +=1

def main(args=None):
    rclpy.init(args=args)
    node = MyFirstNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

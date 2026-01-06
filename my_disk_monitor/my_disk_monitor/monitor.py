#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Ryota Miyauchi
# SPDX-License-Identifier: BSD-3-Clause

import shutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DiskMonitor(Node):
    def __init__(self):
        super().__init__('disk_monitor')
        self.publisher_ = self.create_publisher(Float32, 'disk_usage', 10)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Disk Monitor Node Started')

    def timer_callback(self):
        total, used, free = shutil.disk_usage('/')
        usage_percent = (used / total) * 100

        msg = Float32()
        msg.data = usage_percent
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data:.2f}%')


def main(args=None):
    rclpy.init(args=args)
    disk_monitor = DiskMonitor()
    try:
        rclpy.spin(disk_monitor)
    except KeyboardInterrupt:
        pass
    finally:
        disk_monitor.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

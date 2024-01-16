import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial
import time

class Minibotserial(Node):

    def __init__(self):
        super().__init__('serial')
        self.declare_parameter('arduino_port', '/dev/ttyUSB0') 
        self.declare_parameter("baud_rate", 1000000)
        
        arduino_port = self.get_parameter('arduino_port').value
        baud_rate = self.get_parameter('baud_rate').value
        
        self.ser = serial.Serial(arduino_port, baud_rate)
        time.sleep(3)
        self.get_logger().info('아두이노 연결!!')

        self.publishers_=self.create_publisher(String, '/serial', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        msg = String()
        msg.data = self.ser.readline().decode()
        self.get_logger().info("pub massage: {0}".format(msg.data))
        self.publishers_.publish(msg)

    def connit

def main(args=None):
    rclpy.init(args=args)

    node = Minibotserial()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
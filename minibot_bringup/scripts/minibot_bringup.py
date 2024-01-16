import sys
import rclpy as rp
from rclpy.node import Node

class enable_motors():
    buf = [0xfa, 0xfe, 0x01, 0, 0x1, 0x3, 0, 0xfa, 0xfd]

class cmd():
    buf =[0xfa, 0xfe, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x9, 0x0, 0xfa, 0xfd]

class OdomPose(object):
    x = 0.0
    y = 0.0
    theta = 0.0
    timestamp = 0
    pre_timestamp = 0

class OdomVel(object):
    x = 0.0
    y = 0.0
    w = 0.0

class Joint(object):
    joint_name = ['wheel_left_joint', 'wheel_right_joint']
    joint_pos = [0.0, 0.0]
    joint_vel = [0.0, 0.0]

class Minibotbrinup(Node):
    
    def __init__(self):
        super().__init__('dashboard_client')

        self.odom_pub = 

        self.dsbd_cli = self.create_subscription

        ##rate 1000000




    def send_request(self):
        self.req.req_str = str(sys.argv[1])
        self.future = self.dsbd_cli.call_async(self.req)


def main(args=None):
    rp.init(args=args)
    node = Minibotbrinup()
    rp.spin_once(node)
    node.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()
from example_interfaces.srv import AddTwoInts
from tutorial_interfaces.srv import AddThreeInts

import rclpy
from rclpy.node import Node

class MinimalService(Node):
  def __init__(self):
    super().__init__('minimal_serivce')
    self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
    self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)

  def add_two_ints_callback(self, request, response):
    response.sum = request.a + request.b
    self.get_logger().info('Incomming request\ta: %d b: %d' % (request.a, request.b))

    return response

  def add_three_ints_callback(self, request, response):
    response.sum = request.a + request.b + request.c
    self.get_logger().info('Incomming request\ta: %d b: %d c: %d' % (request.a, request.b, request.c))

    return response
  
def main():
  rclpy.init()
  
  node = MinimalService()
  node.get_logger().info('Service starts…')
  rclpy.spin(node)
  
  rclpy.shutdown()

if __name__ == '__main__':
  main()
  
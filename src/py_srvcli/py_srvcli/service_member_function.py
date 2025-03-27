from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node

class MininumService(Node):
  def __init__(self):
    super().__init__('mininum_serivce')
    self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

  def add_two_ints_callback(self, request, response):
    response.sum = request.a + request.b
    sef.get_logger().info('Incomming request\na: %d b: %d' % (request.a, request.b))

    return response
  
def main():
  rclpy.init()
  node = MinimumSerivce()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == '__main__':
  main()
  
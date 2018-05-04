import socket
import sys
import _thread
import unittest

sys.path.append('lib')

import server

class TestServer(unittest.TestCase):

	def start_server(args):
		server.start()

	def test_port_is_open(self):
		_thread.start_new_thread( self.start_server, () )
		s = socket.socket()

		self.assertIsNone(s.connect(('localhost', 8000)))

if __name__ == '__main__':
	unittest.main()

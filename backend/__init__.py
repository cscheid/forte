# from midi_reader import KeyReader
from server import Server
import sys
sys.path.append('..')

s = Server()
s.serve()

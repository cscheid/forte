# from midi_reader import KeyReader
from server import Server

# reader = KeyReader()
# for k in reader.read():
#     print k

# if __name__ == '__init__':
    

s = Server()
s.serve()

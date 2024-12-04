import pickle
import socket

class Network:
    def __init__(self, argv):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
        if len(argv) > 1: # if not being played on own computer, get the host provided
            self.host = argv[1]
        else:
            hostname = socket.gethostname()
            self.host = socket.gethostbyname(hostname)
        
        self.port = 8999

    def send_data(self, data):
        self.client.send(pickle.dumps(data))
    
    def recieve_data(self):
        self.client.settimeout(.1)

        # Times out unless you have this
        try:
            data = self.client.recv(8192)
        except socket.timeout:
            return None

        return pickle.loads(data)

    def connect_server(self):
        self.client.connect((self.host, self.port))
        
        return pickle.loads(self.client.recv(8192))

    def disconnect_server(self):
        self.client.close()    
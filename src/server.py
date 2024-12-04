import pickle
from _thread import *
from socket import *
from sys import argv

game_instance = {
    'player_turn' : None,
    'players' : [],
    'game_state' : []        
}

def threaded_client(connection, player_id, opp_id, start_game): 
    if start_game:
        connection.send(pickle.dumps(True))
    else:
        connection.send(pickle.dumps(False))

    while True:
        try:
            if game_instance['player_turn'] == player_id:
                send_data = pickle.dumps(game_instance['game_state'])
                connection.send(send_data)

                rec_data = connection.recv(8192)
                game_instance['game_state'] = pickle.loads(rec_data)

                game_instance['player_turn'] = opp_id
        except Exception as e:
            break

    print("Player disconnected")
    connection.close()

if __name__ == '__main__':
    if len(argv) > 1:
        hostIp = argv[1]
    else:
        hostname = gethostname()
        hostIp = gethostbyname(hostname)
    port = 8999

    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((hostIp, port))

    try:
        s.listen(2)
    except error as e:
        print(str(e))
    print("Waiting for a connection...")

    player_queue = None

    while True:
        client, addr = s.accept()
        print(f"Connection from {addr}")

        client_id = len(game_instance['players'])
        game_instance['players'].append(client_id)
        
        if player_queue is not None:
           game_instance['player_turn'] = game_instance['players'][client_id]
           start_new_thread(threaded_client, (client, client_id, player_queue[1], True))
           start_new_thread(threaded_client, (*player_queue, client_id, False))
        else:
           player_queue = (client, client_id)    
import logging
from websocket_server import WebsocketServer



# def new_client(client, server):
#     print("Client(%d) has joined." % client['id'])


# def client_left(client, server):
#     print("Client(%d) disconnected" % client['id'])


def message_back(client, server, message):
    print("Client(%d) said: %s" % (client['id'], message))
    x = int(message.split(',')[0])
    y = int(message.split(',')[1])

    if x>0 and y>0 :
        server.send_message(client,"1")
    if x>0 and y<0 :
        server.send_message(client,"2")
    if x<0 and y<0 :
        server.send_message(client,"3")
    if x<0 and y>0 :
        server.send_message(client,"4")

print(logging,logging.INFO)

server = WebsocketServer(4200, host='', loglevel=logging.INFO)
# server.set_fn_new_client(new_client)
# server.set_fn_client_left(client_left)
server.set_fn_message_received(message_back)
server.run_forever()
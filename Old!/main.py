import requests
from exaroton import Exaroton


def infinite():
    while True:
        yield








for a in infinite():

    cmd = input("GAMC.ONLYKYRO >>")
    if (cmd == "start"):
        Exaroton.start()
    elif (cmd == "stop"):
        Exaroton.stop()
    elif (cmd == "restart"):
        Exaroton.restart()
    elif (cmd == "get_server"):
        Exaroton.get_server()
    elif (cmd == "get_player_list"):
        Exaroton.get_player_list()
    elif (cmd == "get_server_ram"):
        Exaroton.get_server_ram()
    elif (cmd == "help"):
        print("Help command issued:")
        print("[start] -> start the server")
        print("[stop] -> stop the server")
        print("[restart] -> restart the server")
        print("[get_server] -> get info about the server")
        print("[get_player_list] -> see who can join the server")
        print("[get_server_ram] -> see how much ram is allocated to the server")
        print("[help] -> get all the commands")
        print("[end] -> end the program")
        print("info: developed by kyrofx (GitHub) with code from ColinShark's API")
        print("all commands sent via this application can be seen on the console")
        print("this is the limited access version. sudo version is not publicly available")
    elif (cmd == "end"):
        break;
    else:
        print("error: command not found")












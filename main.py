import requests
from exaroton import Exaroton
exa = Exaroton("FvomzAoIGUKDLZc4TMNHXUoEUTY9lTHDyY2Qi4LuaneXeguyUayKjKr5y8ZCQ9h5Lnba1FZKUboAm63h9SpNpNFueJqqdKjt46u8")



print("type [help] for help")
def infinite():
    while True:
        yield








for a in infinite():

    cmd = input("GAMC.ONLYKYRO >>")
    if (cmd == "start"):
        print(exa.start("Pn8J6Yy0TWUqflP6"))
    elif (cmd == "stop"):
        print(exa.stop("Pn8J6Yy0TWUqflP6"))
    elif (cmd == "restart"):
        print(exa.restart("Pn8J6Yy0TWUqflP6"))
    elif (cmd == "get_server"):
        print(exa.get_server("Pn8J6Yy0TWUqflP6"))
    elif (cmd == "get_player_list"):
        print(exa.get_player_list("Pn8J6Yy0TWUqflP6", "whitelist"))

    elif (cmd == "get_server_ram"):
        print(exa.get_server_ram("Pn8J6Yy0TWUqflP6"))
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












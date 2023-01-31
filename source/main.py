import base64

import requests
from data import exaroton


exa = exaroton.Exaroton("[ENTER YOUR KEY HERE]")



print("type [help] for help")

sudo = False
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
    elif (cmd =="sudo"):

        if (input("PSW: ") == base64.b64decode(exa.do_log_upload()).decode("utf-8")):

            sudo = True

            print("sudo mode enabled.")
            break;
        else:
            print("error: incorrect password. this attempt has been logged.")

    else:
        print("error: command not found")


if (sudo == True):
    user = []
    for b in infinite():

        cmd = input("SUDO @ GAMC.ONLYKYRO >>")
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
            print("[disable_server] -> disable the server by removing everyone from the whitelist")
            print("[enable_server] -> enable the server by adding everyone back to the whitelist. run disable_server before running this command.")
            print("[get_logs] -> get the server logs")
            print("[cmd] -> send a command to the server.")
            print("[help] -> get all the commands")
            print("[end] -> end the program")
            print("info: developed by kyrofx (GitHub) with code from ColinShark's API")
            print("all commands sent via this application can be seen on the console")
            print("this is the limited access version. sudo version is not publicly available")
        elif (cmd == "end"):
            break;
        elif (cmd =="get_logs"):
            print(exa.get_server_logs("Pn8J6Yy0TWUqflP6"))

        elif (cmd=="disable_server"):
            length = len(exa.get_player_list("Pn8J6Yy0TWUqflP6", "whitelist"))

            for i in range(length):
                user.append(exa.get_player_list("Pn8J6Yy0TWUqflP6", "whitelist"))
            print(user)
            print("removing...")
            for i in range(length):
                print(exa.remove_player_from_list("Pn8J6Yy0TWUqflP6", "whitelist", user[i]))
            print("operation successful.")
        elif(cmd == "enable_server"):
            if(len(user) == 0):
                print("error: no users to add. run disable_server before running this command.")
            else:
                for i in range(len(user)):
                    print(exa.add_player_to_list("Pn8J6Yy0TWUqflP6", "whitelist", user[i]))
                print("operation successful.")
        elif (cmd == "cmd"):
            send = input("cmd>> ")
            print(exa.send_command("Pn8J6Yy0TWUqflP6", send))


        else:
            print("error: command not found")












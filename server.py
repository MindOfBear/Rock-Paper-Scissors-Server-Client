import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 12345))
s.listen(2)

pServer = 0
pClient = 0
gameOver = False

c, addr = s.accept()
print("S-a realizat conexiunea cu: " + str(addr))

msg = c.recv(1024).decode()
print(msg)

def round():
    global pServer
    global pClient
    global gameOver


    server_move = random.choice(["piatra", "hartie", "foarfeca"])
    print("(DEBUG) Server: " + server_move)

    c.send(b"Serverul este pregatit! Este randul tau!\n(piatra, hartie, foarfeca): ")  # trimite mesajul la client cu info

    move = c.recv(1024).decode()  # primeste alegerea de la client
    print("(DEBUG) Client: " + move)

    if move == server_move:
        result = "Remiza! Ai ales la fel ca serverul!"
    elif (move == "piatra" and server_move == "foarfeca") or (move == "foarfeca" and server_move == "hartie") or (
            move == "hartie" and server_move == "piatra"):
        pClient += 1
        result = "Runda castigata! Serverul a ales: " + server_move + "\nPuncte server: " + str(pServer) + ", puncte client: " + str(pClient)

        if pClient == 2 and pServer == 0 or pClient == 3:
            newMessage = "Ai castigat meciul cu " + str(pClient) + " puncte, serverul a pierdut cu: " + str(pServer)
            c.send(newMessage.encode())
            print("(DEBUG) A castigat client")
            gameOver = True

    else:
        pServer += 1
        result = "Runda pierduta! Serverul a ales: " + server_move + "\nPuncte server: " + str(pServer) + ", puncte client: " + str(pClient)

        if pClient == 0 and pServer == 2 or pServer == 3:
            newMessage = "Ai pierdut meciul cu " + str(pClient) + " puncte, serverul a castigat cu: " + str(pServer)
            c.send(newMessage.encode())
            gameOver = True
            print("(DEBUG) A castigat server")

    print("\n")
    print("(DEBUG) Puncte Client: " + str(pClient))
    print("(DEBUG) Puncte Server: " + str(pServer))
    print("\n")

    c.send(result.encode())  # trimitem mesaju cu win / lose / tie

while gameOver == False:
    round()
c.close() # inchidem




















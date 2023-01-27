import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))



def play_game():
    while True:
        print("\n")
        mesaj = s.recv(1024).decode()
        print(mesaj)
        move = input()
        while move != "foarfeca" and move != "hartie" and move != "piatra":
            print("Ai introdus o valoare gresita! Reintrodu valoarea!\n(piatra, hartie, foarfeca):")
            move = input()
        s.send(move.encode())
        mesaj = s.recv(1024).decode()
        print(mesaj)
        if "meciul" in mesaj:
            break

def start_game():
    print("Introdu START pt a incepe")
    start = input('-> ')
    if start == "START":
        s.send("Debug: Clientul a trimis START".encode())
        play_game()
    else:
        start_game()

start_game()
s.close()
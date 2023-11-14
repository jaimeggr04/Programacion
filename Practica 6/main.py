from usuario import usuario

if __name__ == "__main__":
    user1 = usuario("Jaime", "García", 41920, "Avenida Clara Campoamor 45", "jaimegarciagr@gmail.com", "jaime1234")
    user2 = usuario("Pablo", "Ramirez", 41013, "Aevnida de la borbolla", "pabloramirez@gmail.com", "pablo1234")
    print(user1.mostrarUsuario())
    print(user2.mostrarUsuario())
    user1.check()
    user2.check()


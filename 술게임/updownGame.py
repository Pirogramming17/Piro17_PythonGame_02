import random
import time


def updownGame(self, userName):
    print("""
========================================================================================
_   _ ______         ______  _____  _    _  _   _          _____   ___  ___  ___ _____
| | | || ___ \  ___   |  _  \|  _  || |  | || \ | |        |  __ \ / _ \ |  \/  ||  ___|
| | | || |_/ / ( _ )  | | | || | | || |  | ||  \| | ______ | |  \// /_\ \| .  . || |__
| | | ||  __/  / _ \/\| | | || | | || |/\| || . ` ||______|| | __ |  _  || |\/| ||  __|
| |_| || |    | (_>  <| |/ / \ \_/ /\  /\  /| |\  |        | |_\ \| | | || |  | || |___
\___/ \_|     \___/\/|___/   \___/  \/  \/ \_| \_/         \____/\_| |_/\_|  |_/\____/
========================================================================================
         """)
    print("μμ£Ό λκ»π€― μ μ νμλ μ«μλ₯Ό λ§μΆ°λΌ~! μ«μλ 1οΈβ£ μμ 5οΈβ£ 0οΈβ£ μ¬μ΄~!")

    print("---π’π’π’π’π’---")
    print("--π’π’π’π’π’π’---")
    print("-π’π’βπ’βπ’π’--")
    print("--π’π’π’π’π’π’--")
    print("---π’π’π’π’π’---")
    ans_num = random.randint(1, 50)
    player_length = len(self)
    player_name_list = []
    loser_list = []
    player_choice = ""

    for i in range(player_length):
        if self[i].name == userName:
            player = self[i]
    idx = self.index(player)
    start = 1
    end = 50

    while(1):
        if self[idx % player_length].name == self[0].name:
            while(1):
                if start == end:
                    print("λ¨μ μ«μκ° λ¨ ν κ°ββοΈ")

                player_choice = input("βΆ ν κ°μ§ μ«μλ₯Ό μ ννμμ€ : ")
                player_choice = int(player_choice)
                if(player_choice < start or player_choice > end):
                    print("\nμλ μκΉ κ·Έ λ²μ μλμμμπ€¦ββοΈπ€¦π€¦ββοΈ~~~!! λ°λ³΄ μ·πΊπ€’!")
                    loser_list.append(self[idx % player_length])
                    return loser_list
                else:
                    break
        else:
            player_choice = random.randint(start, end)
            time.sleep(0.3)
            print("{}μ {}μ μ ννμ΅λλ€.".format(
                self[idx % player_length].name, player_choice))

        if player_choice == ans_num:
            print("\n********************************************")
            print("(γγγ­γ)γ μ΄λ΄μκ°... μ λ΅μ {}βοΈβοΈβοΈβοΈβοΈβοΈ Ρ(γγ­γΡ)".format(ans_num))
            print("{}λΉΌκ³  ν μ ν΄πΊ~".format(
                self[idx % player_length].name))
            print("λ§μλΌ λ§μλΌπΆ μ πΊμ΄ λ€μ΄κ°λ€ μ­ μ­μ­μ­μ­πΈπΆ")
            print("********************************************\n")

            for i in range(player_length):
                if i != idx % player_length:
                    loser_list.append(self[i])
            return loser_list
        elif player_choice < ans_num:
            print("UPπΊ\n")
            start = player_choice + 1
            idx += 1
        elif player_choice > ans_num:
            print("DOWNπ»\n")
            end = player_choice - 1
            idx += 1

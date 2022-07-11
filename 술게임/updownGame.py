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
    print("소주 뚜껑🤯 에 적혀있는 숫자를 맞춰라~! 숫자는 1️⃣ 에서 5️⃣ 0️⃣ 사이~!")

    print("---🟢🟢🟢🟢🟢---")
    print("--🟢🟢🟢🟢🟢🟢---")
    print("-🟢🟢❓🟢❓🟢🟢--")
    print("--🟢🟢🟢🟢🟢🟢--")
    print("---🟢🟢🟢🟢🟢---")
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
                    print("남은 숫자가 단 한 개❓❗️")

                player_choice = input("▶ 한 가지 숫자를 선택하시오 : ")
                player_choice = int(player_choice)
                if(player_choice < start or player_choice > end):
                    print("\n아니 아까 그 범위 아니었잖아🤦‍♀️🤦🤦‍♂️~~~!! 바보 샷🍺🤢!")
                    loser_list.append(self[idx % player_length])
                    return loser_list
                else:
                    break
        else:
            player_choice = random.randint(start, end)
            time.sleep(0.3)
            print("{}은 {}을 선택했습니다.".format(
                self[idx % player_length].name, player_choice))

        if player_choice == ans_num:
            print("\n********************************************")
            print("(」゜ロ゜)」 이럴수가... 정답은 {}❗️❗️❗️❗️❗️❗️ щ(゜ロ゜щ)".format(ans_num))
            print("{}빼고 한 잔 해🍺~".format(
                self[idx % player_length].name))
            print("마셔라 마셔라🎶 술🍺이 들어간다 쭊 쭊쭊쭊쭊🎸🎶")
            print("********************************************\n")

            for i in range(player_length):
                if i != idx % player_length:
                    loser_list.append(self[i])
            return loser_list
        elif player_choice < ans_num:
            print("UP🔺\n")
            start = player_choice + 1
            idx += 1
        elif player_choice > ans_num:
            print("DOWN🔻\n")
            end = player_choice - 1
            idx += 1

import time
from User import User
import random


class GameManager:
    def __init__(self):
        self.other_name_list = ["진우", "종욱", "유범", "채은", "동헌"]
        self.player_object_list = []
        self.finish = False

    def play(self):
        self.selectPlayer()
        self.selectComputer()
        self.printResult()
        self.printGame()
        while True:
            for user in self.player_object_list:
                self.chooseGame(self.selectGameNumber(user), user)
                self.printResult()
                self.printGame()

    def selectPlayer(self):
        print("""
        ===================================================================================
        ===================================================================================
        ___   _      _____  _____  _   _  _____  _           _____   ___  ___  ___ _____
        / _ \ | |    /  __ \|  _  || | | ||  _  || |         |  __ \ / _ \ |  \/  ||  ___|
        / /_\ \| |    | /  \/| | | || |_| || | | || |         | |  \// /_\ \| .  . || |__
        |  _  || |    | |    | | | ||  _  || | | || |         | | __ |  _  || |\/| ||  __|
        | | | || |____| \__/\\\ \_/ /| | | |\ \_/ /| |____     | |_\ \| | | || |  | || |___
        \_| |_/\_____/ \____/ \___/ \_| |_/ \___/ \_____/      \____/\_| |_/\_|  |_/\____/
        ===================================================================================
        ===================================================================================
        """)

        my_name = input("🍺 오늘 거하게 취해볼 당신의 이름은? : ")

        print("~~~~~~~~~~~~~~~~~~~~~~~~  🍺 소주 기준 당신의 주량은? 🍺  ~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                          🍺 1. 소주 반병(2잔)")
        print("                          🍺 2. 소주 반병에서 한병(4잔)")
        print("                          🍺 3. 소주 한병에서 한병 반(6잔)")
        print("                          🍺 4. 소주 한병 반에서 두병(8잔)")
        print("                          🍺 5. 소주 두병 이상(10잔)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        while True:
            try:
                my_amount = int(
                    input("🍺 당신의 치사량(주량)은 얼마만큼인가요?(1~5을 선택해주세요) : "))
                if 1 <= my_amount <= 5:
                    break
                else:
                    raise()
            except:
                print()
                print(
                    "<<<<<<<<<<<<<<<<<<<<<<<<<  보기를 다시 선택해주세요!  >>>>>>>>>>>>>>>>>>>>>>>>>")
                print()

        my_amount = 2 * my_amount
        me = User(my_name, my_amount, 0)
        self.player_object_list.append(me)

    def selectComputer(self):
        while True:
            try:
                other_num = int(
                    input("🍺 함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : "))
                if 1 <= other_num <= 3:
                    break
                else:
                    raise()
            except:
                print()
                print(
                    "<<<<<<<<<<<<<<<<<<<<<<<<<  보기를 다시 선택해주세요!  >>>>>>>>>>>>>>>>>>>>>>>>>")
                print()
        other_choice_list = random.sample(self.other_name_list, other_num)
        for i in range(other_num):
            other_amount = 2 * random.randint(1, 5)
            other_name = other_choice_list[i]
            other = User(other_name, other_amount, 0)
            self.player_object_list.append(other)
            print("오늘 함께 취할 친구는 {}입니다! (치사량 : {})".format(
                other_name, other_amount))

    def printGame(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~  🍺 오늘의 Alcohol Game 🍺  ~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                            🍺 1. 게임1")
        print("                            🍺 2. 게임2")
        print("                            🍺 3. 게임3")
        print("                            🍺 4. 게임4")
        print("                            🍺 5. 게임5")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def printResult(self):
        for i in self.player_object_list:
            print("{}(은)는 지금까지 {}🍺! 치사량까지 {}".format(
                i.name, i.now, i.left))
            if i.left == 0:
                self.finish = True
        if self.finish:
            print("{}(이)가 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
            print(
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("                   🍺 다음에 술마시면 또 불러주세요~ 안녕! 🍺                   ")
            print(
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            exit()

    def selectGameNumber(self, user):
        while True:
            if user.name == self.player_object_list[0].name:
                game_choice = int(input("🍺 {}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : ".format(
                    user.name)))
            else:
                continue_key = input(
                    "🍺 술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 'exit'를, 계속하시려면 아무키나 입력해주세요! : ")
                if continue_key == "exit":
                    exit()
                game_choice = random.randint(1, 5)
                print("🍺 {}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : {}".format(
                    user.name, game_choice))

            if game_choice > 5 or game_choice < 1:
                print(
                    "<<<<<<<<<<<<<<<<<<<<<<<<<  보기를 다시 선택해주세요!  >>>>>>>>>>>>>>>>>>>>>>>>>")
            else:
                return game_choice

    def chooseGame(self, num, user):
        if num == 1:
            self.game1()

        elif num == 2:
            self.game2(user)

        elif num == 3:
            self.game3()

        elif num == 3:
            self.game4()

        else:
            self.game5()

    def game1(self):
        return

    def game2(self, user):
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
        player_length = len(self.player_object_list)
        loser_list = []
        player_choice = ""

        now_turn = self.player_object_list.index(user)
        start = 1
        end = 50

        while(1):
            if now_turn % player_length == 0:
                while(1):
                    if start == end:
                        print("남은 숫자가 단 한 개❓❗️")

                    player_choice = input("▶ 한 가지 숫자를 선택하시오 : ")
                    player_choice = int(player_choice)
                    if(player_choice < start or player_choice > end):
                        print("\n아니 아까 그 범위 아니었잖아🤦‍♀️🤦🤦‍♂️~~~!! 바보 샷🍺🤢!")
                        loser_list.append(user)
                        return loser_list
                    else:
                        break
            else:
                player_choice = random.randint(start, end)
                print("{}은 {}을 선택했습니다.".format(
                    self.player_object_list[now_turn % player_length].name, player_choice))

            if player_choice == ans_num:
                print("\n********************************************")
                print("(」゜ロ゜)」 이럴수가... 정답은 {}❗️❗️❗️❗️❗️❗️ щ(゜ロ゜щ)".format(ans_num))
                print("{}빼고 한 잔 해🍺~".format(
                    self.player_object_list[now_turn % player_length].name))
                print("마셔라 마셔라🎶 술🍺이 들어간다 쭊 쭊쭊쭊쭊🎸🎶")
                print("********************************************\n")

                for i in range(player_length):
                    if i != now_turn % player_length:
                        loser_list.append(self.player_object_list[i])
                return loser_list
            elif player_choice < ans_num:
                print("UP🔺\n")
                start = player_choice + 1
                now_turn += 1
            elif player_choice > ans_num:
                print("DOWN🔻\n")
                end = player_choice - 1
                now_turn += 1

    def game3(self):
        return

    def game4(self):
        return

    def game5(self):
        return

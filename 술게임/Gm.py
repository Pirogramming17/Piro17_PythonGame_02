from subwayGame import subwayGame
from updownGame import updownGame
from son import sonGame
from User import User
from apartment2 import aptGame
from TheGameOfDeath import thegameofdeathGame
import random
import time


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
                self.chooseGame(self.selectGameNumber(user), user.name)
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
        print("                            🍺 1. 지하철게임")
        print("                            🍺 2. 술뚜껑 게임")
        print("                            🍺 3. 손병호")
        print("                            🍺 4. 아파트 게임")
        print("                            🍺 5. 더 게임 오브 데스")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def printResult(self):
        for i in self.player_object_list:
            print("{}(은)는 지금까지 {}🍺! 치사량까지 {}".format(
                i.name, i.now, i.left))
            if i.left == 0:
                self.finish = True
                die_name = i.name
        if self.finish:
            print("{}(이)가 전사했습니다...🤢 꿈나라에서🛌는 편히 쉬시길..💤".format(die_name))
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
                time.sleep(1)

            if game_choice > 5 or game_choice < 1:
                print(
                    "<<<<<<<<<<<<<<<<<<<<<<<<<  보기를 다시 선택해주세요!  >>>>>>>>>>>>>>>>>>>>>>>>>")
            else:
                return game_choice

    def drinking(self, user_list):
        for player in self.player_object_list:
            for loser in user_list:
                if player.name == loser.name:
                    player.now += 1
                    player.left = player.amount - player.now

    def chooseGame(self, num, userName):
        if num == 1:
            game1 = subwayGame(self.player_object_list, userName)
            self.drinking(game1.run())

        elif num == 2:
            self.drinking(updownGame(self.player_object_list, userName))

        elif num == 3:
            self.drinking(sonGame(self, userName))

        elif num == 4:
            game4 = aptGame(self.player_object_list, userName)
            self.drinking(game4.play_aptGame())
        else:
            self.drinking(thegameofdeathGame(self, userName))

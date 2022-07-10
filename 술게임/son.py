import random


def sonGame(self, userName):

    question_list = ["연애를 안해본 사람 접어", "오늘 점심 먹은 사람 접어", " 최근에 코딩 공부 한적 있다 접어",
                     " 지금 졸리다 접어", "나는 통학한다 접어", "안경낀 사람 접어", "외로운 사람 접어", " 배고픈 사람 접어", "아이폰쓰는 사람 접어", "운동화 신고 있다 접어",
                     "일요일인데 혼자 있었다 접어", "담배핀다 접어", "피로그래밍 한다 접어", "서울 산다 접어", "지하철 타봤다 접어", "고등학교 다녔다 접어", "남자다 접어",
                     "여자다 접어", "연어 좋아한다 접어", "고기 좋아한다 접어", "모자쓴 사람 접어"]
    com_ans_list = ["Y", "N"]
    loser_li = []
    player_length = len(self.player_object_list)
    player_finger = [5] * player_length

    for i in range(player_length):
        if self.player_object_list[i].name == userName:
            player = self.player_object_list[i]

    print("""
=============================== ================================ ================================ =================          
 _   _                                   _                                  _____                                  
| \ | |                                 | |                                |_   _|                                 
|  \| |  ___ __   __  ___  _ __  ______ | |__    __ _ __   __  ___  ______   | |   ______   ___ __   __  ___  _ __ 
| . ` | / _ \\ \ / / / _ \| '__||______|| '_ \  / _` |\ \ / / / _ \|______|  | |  |______| / _ \\ \ / / / _ \| '__|
| |\  ||  __/ \ V / |  __/| |           | | | || (_| | \ V / |  __/         _| |_         |  __/ \ V / |  __/| |   
\_| \_/ \___|  \_/   \___||_|           |_| |_| \__,_|  \_/   \___|         \___/          \___|  \_/   \___||_|   
=============================== ================================ ================================ =================                                                                                                                                                                                                                                               
""")
    print("손병호 게임을 시작합니다! 질문을 시작하겠습니다!")

    while(True):
        for i in range(player_length):
            if self.player_object_list[i].name == self.player_object_list[0].name:
                print("질문과 함께 (Y/N)으로 답해주세요!")
                user_qus = input("질문: ")
                ans = input("답변 : ")
                if ans == "Y":
                    player_finger[0] -= 1
                else:
                    pass
                    ans = input("Y와 N중에 골라주세요: ")
                for j in range(1, player_length):
                    com_ans = random.choice(com_ans_list)
                    if com_ans == "Y":
                        player_finger[j] -= 1
                        print("{}님은 'Y' 을 고르셨습니다.".format(
                            self.player_object_list[j].name))
                    else:
                        print("{}님은 'N' 을 고르셨습니다.".format
                              (self.player_object_list[j].name))
            else:
                com_qus = random.choice(question_list)
                ans = input(com_qus+"(Y/N ??)")
                question_list.remove(com_qus)
                if ans == "Y":
                    player_finger[0] -= 1
                else:
                    pass
                for j in range(1, player_length):
                    com_ans = random.choice(com_ans_list)
                    if com_ans == "Y":
                        player_finger[j] -= 1
                        print("{}님은 'Y' 을 고르셨습니다.".format(
                            self.player_object_list[j].name))
                    else:
                        print("{}님은 'N' 을 고르셨습니다.".format
                              (self.player_object_list[j].name))
            for k in range(len(player_finger)):
                print(
                    self.player_object_list[k].name+"의 목숨은 {}개!".format(player_finger[k]))
                if player_finger[k] == 0:
                    loser_li.append(self.player_object_list[k])
                    return loser_li
        print("여기")

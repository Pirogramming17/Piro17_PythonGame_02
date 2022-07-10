import random


def

question_list = ["연애를 안해본 사람 접어", "오늘 점심 먹은 사람 접어", " 최근에 코딩 공부 한적 있다 접어",
 " 지금 졸리다 접어","나는 통학한다 접어","안경낀 사람 접어","외로운 사람 접어", " 배고픈 사람 접어","아이폰쓰는 사람 접어","운동화 신고 있다 접어",
 "일요일인데 혼자 있었다 접어","담배핀다 접어","피로그래밍 한다 접어","서울 산다 접어","지하철 타봤다 접어","고등학교 다녔다 접어","남자다 접어",
 "여자다 접어","연어 좋아한다 접어","고기 좋아한다 접어","모자쓴 사람 접어"]
com_ans_list =["Y","N"]
player_finger = []
loser_li =[]
player_length = len(self.player_object_list)
computer_length = len(self.other_choice_list)




for i in range(player_length):
    if self[i].name == userName:
        player= self[i]
    player_finger[i].append(int(5))



print("손병호 게임을 시작합니다! 질문을 시작하겠습니다!")



while(True):
    for i in self.player_object_list:
        if self.player_object_list[i] == player:
            print("질문과 함께 (Y/N)으로 답해주세요!")
            user_qus = input("질문: \n")
            ans =input(" 답변 : \n")
            if ans == "Y":
                player_finger[i] -= 1
            else:
                pass
                ans = input("Y와 N중에 골라주세요: ")
            for j in self.player_object_list[1:]:
                com_ans = random.choice(com_ans_list)
                if com_ans == "Y":
                    player_finger[j] -= 1
                    print(" %c 님은 'Y' 을 고르셨습니다." %(self[j].name))
                else:
                    print(" %c 님은 'N' 을 고르셨습니다." %(self[j].name))
            for k in player_finger:
                print(self[k].name+"의 목숨은 %d개!" %player_finger[k])
                if player_finger[k] == 0:
                    loser_li.append(self[k])
                    break     
        else:
            com_qus = random.choice(question_list)
            ans =  input(com_qus+"(Y/N ??)")
            question_list = question_list.remove(com_qus)
            if ans == "Y":
                player_finger[i] -= 1
            else:
                pass
            for j in self.player_object_list[1:]:
                com_ans = random.choice(com_ans_list)
                if com_ans == "Y":
                    player_finger[j] -= 1
                    print(" %c 님은 'Y' 을 고르셨습니다." %(self[j].name))
                else:
                    print(" %c 님은 'N' 을 고르셨습니다." %(self[j].name))
            for k in player_finger:
                if player_finger[k] == 0:
                    loser_li.append(self[k])
                    break
    if 0 in player_finger:
        break


return loser_li
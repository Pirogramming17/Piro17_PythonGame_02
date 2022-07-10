import random


class aptGame:
    def __init__(self, apt_player_list, selector):
        self.apt_player_list = apt_player_list
        self.selector = selector

    def play_aptGame(self):
        print("""
        =============================================================================================
          ___                       _                            _     _____                         
         / _ \                     | |                          | |   |  __ \                        
        / /_\ \ _ __    __ _  _ __ | |_  _ __ ___    ___  _ __  | |_  | |  \/  __ _  _ __ ___    ___ 
        |  _  || '_ \  / _` || '__|| __|| '_ ` _ \  / _ \| '_ \ | __| | | __  / _` || '_ ` _ \  / _ \
        | | | || |_) || (_| || |   | |_ | | | | | ||  __/| | | || |_  | |_\ \| (_| || | | | | ||  __/
        \_| |_/| .__/  \__,_||_|    \__||_| |_| |_| \___||_| |_| \__|  \____/ \__,_||_| |_| |_| \___|
            | |                                                                                   
            |_|                                                                                   
        =============================================================================================
        """)
        print("아파트 게임을 시작합니다! 아파트의 층수를 입력해주세요.(10~50 사이의 정수)")
        if self.apt_player_list[0].name == self.selector:
            while True:
                apt_floor = int(input())
                if apt_floor > 50 or apt_floor < 10 or type(apt_floor) != int:
                    print("10~50 사이의 정수를 입력해주세요")
                else:
                    break
        else:
            apt_floor = random.randint(10, 50)
        print("아파트는", apt_floor, "층!")
        player_length = len(self.apt_player_list)
        random.shuffle(self.apt_player_list)
        now_floor = 0
        apt_loser = None
        while True:
            for i in range(player_length):
                now_floor += 1
                print(self.apt_player_list[i].name, ':', now_floor, '층')
                if now_floor == apt_floor:
                    apt_loser = self.apt_player_list[i]  # loser변수에 패배한 사람 기록.
                    break
            if now_floor == apt_floor:
                break
        print("패배자는", apt_loser.name, "당첨~!🍺🍺🍺")
        print("마셔라 마셔라🎶 술🍺이 들어간다 쭊 쭊쭊쭊쭊🎸🎶")
        print("********************************************")
        return [apt_loser]

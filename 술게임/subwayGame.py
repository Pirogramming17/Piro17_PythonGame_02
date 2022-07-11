from bs4 import BeautifulSoup as bs
import random
import requests
import warnings
import time
warnings.filterwarnings('ignore')


class subwayGame:
    def __init__(self, player_list, selector) -> None:
        self.station = []
        self.player_list = player_list
        self.selector = selector
        self.storestation = []

    def run(self) -> None:
        print("""
================================================================================              
 _____  _   _ ______  _    _   ___  __   __         _____   ___  ___  ___ _____ 
/  ___|| | | || ___ \| |  | | / _ \ \ \ / /        |  __ \ / _ \ |  \/  ||  ___|
\ `--. | | | || |_/ /| |  | |/ /_\ \ \ V /  ______ | |  \// /_\ \| .  . || |__  
 `--. \| | | || ___ \| |/\| ||  _  |  \ /  |______|| | __ |  _  || |\/| ||  __| 
/\__/ /| |_| || |_/ /\  /\  /| | | |  | |          | |_\ \| | | || |  | || |___ 
\____/  \___/ \____/  \/  \/ \_| |_/  \_/           \____/\_| |_/\_|  |_/\____/ 
================================================================================                                                                                
"""
              )
        self.collectStations()
        print("지/\하철/\🚇~ 지하철 지/\하철/\🚇 지하철~")
        if self.player_list[0].name == self.selector:
            lineNum = int(input("몇 호선~❓❗️ 몇 호선~❓❗️: "))
            print("{} 호선 /\ {} 호선 /\~❗️ {} 호선 /\ {} 호선 /\~❗️".format(lineNum,
                  lineNum, lineNum, lineNum))
        else:
            lineNum = random.randint(1, 9)
            print("몇 호선~❓❗️ 몇 호선~❓❗️: ")
            print("{} 호선 /\ {} 호선 /\~❗️ {} 호선 /\ {} 호선 /\~❗️".format(lineNum,
                  lineNum, lineNum, lineNum))

        while True:
            for i in range(len(self.player_list)):
                if i == 0:
                    stationName = [
                        input("{} 호선 역 이름({}): ".format(lineNum, self.player_list[i].name))]

                else:
                    probability = random.randint(1, 5)
                    if probability > 4:
                        while True:
                            wrongLine = random.randint(1, 9)
                            if wrongLine != lineNum:
                                break
                        stationName = random.choice(
                            self.station[wrongLine - 1])
                    else:
                        stationName = random.choice(self.station[lineNum - 1])
                    print("{} 호선 역 이름({}): {}".format(
                        lineNum, self.player_list[i].name, "".join(s for s in stationName)))

                if not self.checkStation(stationName, lineNum):
                    print("\n********************************************")
                    print("{} 당첨~❗️❗️❗️❗️🍺🍺🍺".format(self.player_list[i].name))
                    print("마셔라 마셔라🎶 술🍺이 들어간다 쭊 쭊쭊쭊쭊🎸🎶")
                    print("********************************************\n")
                    return [self.player_list[i]]

    def collectStations(self) -> None:
        for i in range(1, 10):
            url = "http://openapi.seoul.go.kr:8088/4972485a4b61727538335863426167/xml/SearchSTNBySubwayLineInfo/1/150/%20/%20/{}%ED%98%B8%EC%84%A0".format(
                i)
            req = requests.get(url)
            sp = bs(req.text, "html.parser")

            stationList = [el.text.split(",")
                           for el in sp.select("row > station_nm")]
            self.station.append(stationList)

    def checkStation(self, station, lineNum) -> bool:
        for stationLine in self.station[lineNum - 1]:
            if stationLine == station:
                if self.storestation == []:
                    self.storestation.append(station)
                    return True
                for i in self.storestation:
                    if i == station:
                        return False
                self.storestation.append(station)
                return True

        return False

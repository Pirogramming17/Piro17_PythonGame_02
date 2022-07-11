import random
import time


def thegameofdeathGame(self, userName):
    print("""
===============================================================================================================
 _____  _                ___                                _____    ___     ___                  _    _     
(_   _)( )              (  _`\                             (  _  ) /'___)   (  _`\               ( )_ ( )    
  | |  | |__     __     | ( (_)   _ _   ___ ___     __     | ( ) || (__     | | ) |   __     _ _ | ,_)| |__  
  | |  |  _ `\ /'__`\   | |___  /'_` )/' _ ` _ `\ /'__`\   | | | || ,__)    | | | ) /'__`\ /'_` )| |  |  _ `\\
  | |  | | | |(  ___/   | (_, )( (_| || ( ) ( ) |(  ___/   | (_) || |       | |_) |(  ___/( (_| || |_ | | | |
  (_)  (_) (_)`\____)   (____/'`\__,_)(_) (_) (_)`\____)   (_____)(_)       (____/'`\____)`\__,_)`\__)(_) (_)                                                                                                                                                                                                                         
===============================================================================================================
""")

    gm5_player_list = random.sample(
        self.player_object_list, len(self.player_object_list))

    print("""{}님이 술래입니다 깔깔 😄
~~~~~~~~ 아 신난다😊 ~❗️ 아싸~ 재미난다😆 ~ 아싸~❗️ 더 게임 오브 데스  ~~~~~~~~
""".format(gm5_player_list[0].name))
    while True:
        try:
            num_point = int(input('2️⃣ 이상 8️⃣ 이하의 정수를 외쳐주세요❗️ :'))
            if 2 <= num_point <= 8:
                break
            else:
                raise()
        except:
            print("<<<<<<<<<<<<<<<<<<<  2️⃣ 이상 8️⃣ 이하의 정수를 외쳐주세요❗️  >>>>>>>>>>>>>>>>>>>")

    nom_list = []
    penalty_list = []

    for i in range(len(gm5_player_list)):
        time.sleep(0.3)
        if i < len(gm5_player_list)-1:
            print("{} 👉 {}".format(
                gm5_player_list[i].name, gm5_player_list[i+1].name))
            nom_list.append(gm5_player_list[i+1])
        else:
            print("{} 👉 {}".format(
                gm5_player_list[i].name, gm5_player_list[0].name))
            nom_list.append(gm5_player_list[0])
    print()
    time.sleep(0.5)
    for i in range(num_point):
        time.sleep(0.3)
        if i < len(nom_list):
            print("{} :".format(
                gm5_player_list[i].name), i+1, " ☠️👉 {} ".format(nom_list[i].name))
            penalty = nom_list[i]
        elif len(nom_list) <= i < 2*len(nom_list):
            print("{} :".format(
                gm5_player_list[i-len(nom_list)].name), i+1, " ☠️👉 {} ".format(nom_list[i-len(nom_list)].name))
            penalty = nom_list[i-len(nom_list)]
        else:
            print("{} :".format(
                gm5_player_list[i-len(nom_list)*2].name), i+1, " ☠️👉 {} ".format(nom_list[i-len(nom_list)*2].name))
            penalty = nom_list[i-len(nom_list)*2]
    print("\n********************************************")
    print(penalty.name, ": 깔깔🍻 당첨~❗️❗️❗️❗️🍺🍺🍺")
    print("마셔라 마셔라🎶 술🍺이 들어간다 쭊 쭊쭊쭊쭊🎸🎶")
    print("********************************************\n")
    penalty_list.append(penalty)

    return penalty_list

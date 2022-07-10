import random


def thegameofdeathGame(self, userName):
    print("""
==================================================================================================================================================================
ooooooooooooo oooo                      .oooooo.                                                      .o88o.  oooooooooo.                            oooo
8'   888   `8 `888                     d8P'  `Y8b                                                     888 `"  `888'   `Y8b                      .o8  `888
     888       888 .oo.    .ooooo.    888           .oooo.   ooo. .oo.  .oo.    .ooooo.     .ooooo.  o888oo    888      888  .ooooo.   .oooo. .o888oo 888 .oo.
     888       888P"Y88b  d88' `88b   888          `P  )88b  `888P"Y88bP"Y88b  d88' `88b   d88' `88b  888      888      888 d88' `88b `P  )88b  888   888P"Y88b
     888       888   888  888ooo888   888     ooooo .oP"888   888   888   888  888ooo888   888   888  888      888      888 888ooo888  .oP"888  888   888   888
     888       888   888  888    .o   `88.    .88' d8(  888   888   888   888  888    .o   888   888  888      888     d88' 888    .o d8(  888  888 . 888   888
    o888o     o888o o888o `Y8bod8P'    `Y8bood8P'  `Y888""8o o888o o888o o888o `Y8bod8P'   `Y8bod8P' o888o    o888bood8P'   `Y8bod8P' `Y888""8o "888" o888o o888o
==================================================================================================================================================================
""")

    gm5_player_list = random.sample(
        self.player_object_list, len(self.player_object_list))

    print("""{}님이 술래입니다 깔깔 😄
~~~~~~~~ 아 신난다 😊 재미난다 😆 더 게임 오브 데스  ~~~~~~~~
""".format(gm5_player_list[0].name))
    while True:
        try:
            num_point = int(input('2 이상 8 이하의 정수를 외쳐주세요! :'))
            if 2 <= num_point <= 8:
                break
            else:
                raise()
        except:
            print("<<<<<<<<<<<<<<<<<<<  2 이상 8 이하의 정수를 외쳐주세요!  >>>>>>>>>>>>>>>>>>>")

    nom_list = []
    penalty_list = []

    for i in range(len(gm5_player_list)):
        if i < len(gm5_player_list)-1:
            print("{} 👉 {}".format(
                gm5_player_list[i].name, gm5_player_list[i+1].name))
            nom_list.append(gm5_player_list[i+1])
        else:
            print("{} 👉 {}".format(
                gm5_player_list[i].name, gm5_player_list[0].name))
            nom_list.append(gm5_player_list[0])

    for i in range(num_point):
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
    print(penalty.name, ": 깔깔🍻")
    penalty_list.append(penalty)

    return penalty_list

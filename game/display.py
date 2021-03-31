from game import constants

import arcade

class Display():
    def __init__(self):
        super().__init__()
        
        


    def hud(self, cast):
        player_1 = cast["player"][0]
        player_2 = cast["player"][1]
        arcade.draw_text(f"{round(player_1.damage * 35)}%", 5,600, arcade.color.BLACK, 30, font_name='BERNHC')
        player_2_damage = round(player_2.damage * 35)
        if len(str(player_2_damage)) == 3:
            x = 915
        elif len(str(player_2_damage)) == 1:
            x = 950
        elif len(str(player_2_damage)) == 2:
            x = 933
        else: 
            x = 915
        arcade.draw_text(f"{player_2_damage}%", x,600, arcade.color.BLACK, 30, font_name='BERNHC')
        texture = arcade.load_texture(":resources:images/items/coinGold_lr.png")
        scale = .4
        if player_1.lives == 3:
            lives_1 = 76
        elif player_1.lives == 2:
            lives_1 = 41
        elif player_1.lives == 1:
            lives_1 = 6
        else: 
            lives_1 = 0 
        for i in range(5, lives_1, 35):
            arcade.draw_scaled_texture_rectangle(i, 590, texture, scale, 0)

        if player_2.lives == 3:
            lives_2 = 899
        elif player_2.lives == 2:
            lives_2 = 934
        elif player_2.lives == 1:
            lives_2 = 969
        else: 
            lives_2 = 971

        for i in range(970, lives_2, -35):
            arcade.draw_scaled_texture_rectangle(i, 590, texture, scale, 0)
        
        



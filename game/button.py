import arcade
import arcade.gui

class Button(arcade.gui.UIImageButton):

    NORMAL = arcade.load_texture(':resources:gui_basic_assets/red_button_normal.png')

    HOVER = arcade.load_texture(':resources:gui_basic_assets/red_button_hover.png')

    PRESS = arcade.load_texture(':resources:gui_basic_assets/red_button_press.png')
        
    def __init__(self, text, center_x, center_y, width, height):
        super().__init__(text=text, center_x=center_x, center_y=center_y, 
            normal_texture=Button.NORMAL, hover_texture=Button.HOVER,
            press_texgure=Button.PRESS)
import arcade
import arcade.gui


class Button(arcade.gui.UIImageButton):

    # NORMAL = arcade.load_texture(':resources:gui_basic_assets/red_button_normal.png')

    # HOVER = arcade.load_texture(':resources:gui_basic_assets/red_button_hover.png')

    # PRESS = arcade.load_texture(':resources:gui_basic_assets/red_button_press.png')
        
    def __init__(self, text, center_x, center_y, width, height):
        self.NORMAL = arcade.load_texture(':resources:gui_basic_assets/red_button_normal.png')

        self.HOVER = arcade.load_texture(':resources:gui_basic_assets/red_button_hover.png')

        self.PRESS = arcade.load_texture(':resources:gui_basic_assets/red_button_press.png')
        
        super().__init__(text=text, center_x=center_x, center_y=center_y, 
            normal_texture=self.NORMAL, hover_texture=self.HOVER,
            press_texgure=self.PRESS)
            
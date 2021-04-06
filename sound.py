import arcade 


class Sound(arcade.Sound):
    def __init__(self):
        pass



    def theme_music(self):
        arcade.play_sound(arcade.load_sound("art/background.wav"))

    def stop(self, media):
        arcade.stop_sound(media)
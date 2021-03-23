class Sprite():
    def __init__(self):
        self.__position = None
        self.__velocity = None
        self.__icon = None

# setters
    def set_position(self, x, y):
        self.__position = (x,y)

    def set_velocity(self, x, y):
        self.__velocity = (x,y)

    def set_icon(self, icon):
        self.__icon = icon

# getters
    def get_position(self):
        return self.__position

    def get_velocity(self):
        return self.__velocity

    def set_icon(self):
        return self.__icon

# other methods
    def move(self):
        x1 = self.__position[0]
        y1 = self.__position[1]
        x2 = self.__position[0] + self.__velocity[0]
        y2 = self.__position[1] + self.__velocity[1]

        self.__position = (x2, y2)
class Player:
    def __init__(self, startX, startY, dir):
            self.x=startX
            self.y=startY
            self.deltaX=0
            self.deltaY=0
            self.speed=11
            self.score= 0
            self.dirY="down"
            self.dirX=dir

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
        if(x > 1049):
                x = -175

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def deltaX(self):
        return self.__deltaX

    @deltaX.setter
    def deltaX(self, deltaX):
        self.__deltaX = deltaX

    @property
    def deltaY(self):
        return self.__deltaY

    @deltaY.setter
    def deltaY(self, deltaY):
        self.__deltaY = deltaY

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def deltaX(self, speed):
        self.__speed = speed

    @property
    def score(self):
        return self.__score

    @score.setter
    def deltaY(self, score):
        self.__score = score

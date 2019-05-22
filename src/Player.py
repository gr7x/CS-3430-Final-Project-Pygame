import Const
class Player:
    def __init__(self, startX, startY, dir):
            self._x=startX
            self._y=startY
            self._deltaX=0
            self._deltaY=0
            self._speed=12
            self._score= 0
            self._dirY="down"
            self._dirX=dir

    @property
    def x(self):
            return self._x

    @x.setter
    def x(self, x):
        if(x >= 250 and x <= Const.SCREEN_WIDTH-450):
            self._x = x
        elif(x < 250):
            self._x = 250
        elif(x > Const.SCREEN_WIDTH-450):
            self._x = Const.SCREEN_WIDTH-450

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def deltaX(self):
        return self._deltaX

    @deltaX.setter
    def deltaX(self, deltaX):
        self._deltaX = deltaX

    @property
    def deltaY(self):
        return self._deltaY

    @deltaY.setter
    def deltaY(self, deltaY):
        self._deltaY = deltaY

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def deltaX(self, speed):
        self._speed = speed

    @property
    def score(self):
        return self._score

    @score.setter
    def deltaY(self, score):
        self._score = score

        #--HERE
    @property
    def dirY(self):
        return self._dirY

    @dirY.setter
    def dirY(self, dirY):
        self._sdirY = dirY

    @property
    def dirX(self):
        return self._dirX

    @dirX.setter
    def dirX(self, dirX):
        self._dirX = dirX

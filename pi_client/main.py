import pyxel

APP_WIDTH: int = 480 // 2
APP_HEIGHT: int = 320 // 2

class Panel:
    def __init__(self, x: int, y: int, w: int, h: int, name: str, bg_color = pyxel.COLOR_PINK) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
        self.bg_color = bg_color

    def update(self):
        pass

    def off_x(self, off: int):
        return self.x + off

    def off_y(self, off: int):
        return self.y + off

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.bg_color)
        pyxel.text(self.off_x(2), self.off_y(1), self.name, pyxel.COLOR_WHITE)

class App:
    def __init__(self):
        self.left = Panel(0, 0, APP_WIDTH // 2, APP_HEIGHT, "Victoria")
        self.right = Panel(APP_WIDTH // 2 + 1, 0, APP_WIDTH // 2, APP_HEIGHT, "Michael", bg_color=pyxel.COLOR_LIGHT_BLUE)


        pyxel.init(APP_WIDTH, APP_HEIGHT, title="Hello Pyxel")
        pyxel.fullscreen(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIGHT_BLUE)

        self.left.draw()
        self.right.draw()

        pyxel.line(APP_WIDTH // 2 , 0, APP_WIDTH // 2 , APP_HEIGHT, pyxel.COLOR_WHITE)



App()

import pyxel

APP_WIDTH: int = 480
APP_HEIGHT: int = 320

class App:
    def __init__(self):
        pyxel.init(APP_WIDTH, APP_HEIGHT, title="Hello Pyxel")
        pyxel.fullscreen(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        radius = 100 

        pyxel.circb(100 * pyxel.cos(pyxel.frame_count) + APP_WIDTH / 2, 100 * pyxel.sin(pyxel.frame_count) + APP_HEIGHT / 2, 5, pyxel.COLOR_WHITE)

        pyxel.circb(APP_WIDTH / 2, APP_HEIGHT / 2, radius, pyxel.COLOR_WHITE)
        pyxel.circb(APP_WIDTH / 2, APP_HEIGHT / 2, radius * 0.75, pyxel.COLOR_WHITE)
        pyxel.circb(APP_WIDTH / 2, APP_HEIGHT / 2, radius * 0.50, pyxel.COLOR_WHITE)
        pyxel.circb(APP_WIDTH / 2, APP_HEIGHT / 2, radius * 0.25, pyxel.COLOR_WHITE)


App()

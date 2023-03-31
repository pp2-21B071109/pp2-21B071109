import pygame as pg
pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('black')
BLUE = pg.Color('white')
pg.mixer.music.load(r'C:\Users\Iskander\Desktop\git_tutorial\work\hello\tsis7\track1.mp3')
pg.mixer.music.play(-1)
button = pg.Rect(100, 150, 90, 30)
music_paused = False
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                # Toggle the boolean variable.
                music_paused = not music_paused
                if music_paused:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
    screen.fill(BG_COLOR)
    pg.draw.rect(screen, BLUE, button)
    pg.display.flip()
    clock.tick(60)
pg.quit()
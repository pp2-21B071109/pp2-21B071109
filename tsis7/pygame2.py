import pygame

pygame.init()
width = 800
height = 700

screen = pygame.display.set_mode((width , height))
pygame.display.set_caption('DJ music')
icon = pygame.image.load(r"C:\Users\Iskander\Desktop\git_tutorial\work\hello\tsis7\iconca.png")
pygame.display.set_icon(icon)
cover = pygame.image.load(r'C:\Users\Iskander\Desktop\git_tutorial\work\hello\tsis7\cover.jpg')
new_cover = pygame.transform.scale(cover, (800, 700))
player = pygame.image.load(r'C:\Users\Iskander\Desktop\git_tutorial\work\hello\tsis7\player.png')
new_player = pygame.transform.scale(player, (400, 100))


music_sound = [
    pygame.mixer.Sound(r'C:\Users\Iskander\Desktop\git_tutorial\work\hello\tsis7\track1.mp3'),
    pygame.mixer.Sound(r'C:\Users\Iskander\Desktop\git_tutorial\work\hello\tsis7\track2.mp3'),
    pygame.mixer.Sound(r'C:\Users\Iskander\Desktop\git_tutorial\work\hello\tsis7\track3.mp3')
]


selected_sound_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                music_sound[selected_sound_index].play()
            elif event.key == pygame.K_DOWN:
                music_sound[selected_sound_index].stop()
            elif event.key == pygame.K_LEFT:
                music_sound[selected_sound_index].stop()
                selected_sound_index = (selected_sound_index - 1) % len(music_sound)
                music_sound[selected_sound_index].play()
            elif event.key == pygame.K_RIGHT:
                music_sound[selected_sound_index].stop()
                selected_sound_index = (selected_sound_index + 1) % len(music_sound)
                music_sound[selected_sound_index].play()

    screen.blit(new_cover, (0, 0))
    screen.blit(new_player, (200, 600))
    pygame.display.update()
import pygame, os, sys
from overworld import Overworld
pygame.font.init()
pygame.mixer.init()

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 1056, 594
charHeight = 60
charWidth = charHeight//2
Vel = 5
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Leads to Rome Test 1 - 2/09/2022 - James Serrano")
mainCharacterImage = pygame.image.load(os.path.join(
    'sensei.png'))
mainCharacter = pygame.transform.scale(mainCharacterImage, (charWidth, charHeight))

class Game:
    def __init__(self, ThePilgrim):
        self.overworld = Overworld(WIN, ThePilgrim)
    
    def run(self, ThePilgrim):
        #keys_pressed = pygame.key.get_pressed()
        #moveMC(keys_pressed, ThePilgrim)
        #drawWindow(ThePilgrim)
        self.overworld.run(ThePilgrim)




def drawWindow(ThePilgrim):
    #WIN.fill(SAND)
    WIN.blit(mainCharacter, (ThePilgrim.x, ThePilgrim.y))
    pygame.display.update()

def moveMC(keys_pressed, ThePilgrim):
    if keys_pressed[pygame.K_a] and ThePilgrim.x - Vel >= 0:
        ThePilgrim.x -= Vel
    if keys_pressed[pygame.K_d] and ThePilgrim.x + charWidth + Vel <= 1056:
        ThePilgrim.x += Vel
    if keys_pressed[pygame.K_w] and ThePilgrim.y -Vel >= 0:
        ThePilgrim.y -= Vel
    if keys_pressed[pygame.K_s] and ThePilgrim.y + charHeight + Vel <= 594:
        ThePilgrim.y += Vel



def main():

    ThePilgrim = pygame.Rect(SCREEN_WIDTH//2 -charWidth//2, SCREEN_HEIGHT//2 - charHeight//2, charWidth, charHeight)
    game = Game(ThePilgrim)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.run(ThePilgrim)
        #keys_pressed = pygame.key.get_pressed()
        #moveMC(keys_pressed, ThePilgrim)
        #drawWindow(ThePilgrim)

    pygame.quit()

if __name__ == "__LeadsToRomeTest__":
    main()

else:
    main()
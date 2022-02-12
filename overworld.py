import pygame, os
from gameData import levels


Globalx = 0
Globaly = 0
SCREEN_WIDTH, SCREEN_HEIGHT, Vel = 1056, 594, 5
SAND = (194, 178, 128)
charHeight = 60
charWidth = charHeight //2 
mainCharacterImage = pygame.image.load(os.path.join(
    'sensei.png'))
mainCharacter = pygame.transform.scale(mainCharacterImage, (charWidth, charHeight))

def moveMC(keys_pressed, ThePilgrim, Nodes):
    if keys_pressed[pygame.K_a] and ThePilgrim.x - Vel >= 0:
        for nodeData in Nodes:
            nodeData.x += Vel
    if keys_pressed[pygame.K_d] and ThePilgrim.x + charWidth + Vel <= 1056:
        for nodeData in Nodes:
            nodeData.x -= Vel
    if keys_pressed[pygame.K_w] and ThePilgrim.y -Vel >= 0:
        for nodeData in Nodes:
            nodeData.y += Vel
    if keys_pressed[pygame.K_s] and ThePilgrim.y + charHeight + Vel <= 594:
        for nodeData in Nodes:
            nodeData.y -= Vel

def drawNodes(surface, Nodes):
    for nodeData in Nodes:
        surface.blit(nodeData.image, (nodeData.x, nodeData.y))


class Node(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((100, 80))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)

class Overworld:
    def __init__(self, surface, ThePilgrim):
        self.display_surface = surface
        self.setup_nodes()
        self.display_surface.fill(SAND)

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for node_data in levels.values():
            node_sprite = Node(node_data['node_pos'])
            node_sprite.x = node_data['node_pos'][0]
            node_sprite.y = node_data['node_pos'][1]

            self.nodes.add(node_sprite)

    def run(self, ThePilgrim):
        
        keys_pressed = pygame.key.get_pressed()
        moveMC(keys_pressed, ThePilgrim, self.nodes)
        self.display_surface.fill(SAND)
        drawNodes(self.display_surface, self.nodes)
        #self.nodes.draw(self.display_surface)
        self.display_surface.blit(mainCharacter, (ThePilgrim.x, ThePilgrim.y))
        pygame.display.update()
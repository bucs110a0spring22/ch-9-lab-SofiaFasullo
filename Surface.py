import pygame

class Surface(pygame.sprite.Sprite):
  def __init__(self, filename, x, y, h, w):
    self.image = pygame.image.load(filename)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.rect.height = h
    self.rect.width = w
    

  def getRect(self):
    return self.rect
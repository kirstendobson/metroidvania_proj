import pygame as pg
import random
from settings import *
from sprites import *

from pygame.locals import (
  RLEACCEL,
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_ESCAPE,
  KEYDOWN,
  QUIT,
)

class Game:
  def __init__(self):
    # Initialize Game
    pg.mixer.init()
    pg.init()
    self.screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(TITLE)
    self.clock = pg.time.Clock()
    self.running = True

  def new(self):
    # start a new game
    self.all_sprites = pg.sprite.Group()
    self.platforms = pg.sprite.Group()
    self.player = Player(self)
    self.all_sprites.add(self.player)
    # ground platform
    p1 = Platform(0, HEIGHT-40, WIDTH, 40)
    self.all_sprites.add(p1)
    self.platforms.add(p1)
    # raised platform
    p2 = Platform(WIDTH/2 - 50, HEIGHT * 3/4, 100, 20)
    self.all_sprites.add(p2)
    self.platforms.add(p2)
    self.run()
    

  def run(self):
    # Game loop
    self.playing = True
    while self.playing:
      self.clock.tick(FPS)
      self.events()
      self.update()
      self.draw()

  def update(self):
    # Game Loop - Update
    self.all_sprites.update()
    # platform detection if falling
    if self.player.vel.y > 0:
      hits = pg.sprite.spritecollide(self.player, self.platforms, False)
      if hits:
        self.player.pos.y = hits[0].rect.top
        self.player.vel.y = 0

  def events(self):
    # Game Loop - events
      for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
          if self.playing:
            self.playing = False
          self.running = False
        
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_SPACE:
            self.player.jump()

  def draw(self):
    #Game Loop - draw 
    self.screen.fill(BLACK)
    self.all_sprites.draw(self.screen)
    pg.display.flip()


  def show_start_screen(self):
    # game splash/start screen
    pass

  def show_go_screen(self):
    #game over/continue
    pass

g = Game()
g.show_start_screen()
while g.running:
  g.new()
  g.show_go_screen()

pg.quit()
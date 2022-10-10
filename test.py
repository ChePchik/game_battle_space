import unittest
import pygame
from settings import Settings
from button import Button

class Testing_game(unittest.TestCase):

  def test_1(self):
    self.assertEqual(2,1+1)
    print(1)

    def test_2(self):
      pygame.init()
      ai_settings = Settings()
      screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
      pygame.display.set_caption("Space Battle")
      play_button = Button(ai_settings, screen, "For a fight!")

if __name__ == "__main__":
  unittest.main()
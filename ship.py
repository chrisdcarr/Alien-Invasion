
import pygame

class Ship:

	def __init__(self,ai_game):
		""" init the ship and set starting pos"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#load ship img and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		"""draw the ship in cur location"""
		self.screen.blit(self.image,self.rect)


import pygame

class Ship:

	def __init__(self,ai_game):
		""" init the ship and set starting pos"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings

		#load ship img and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		#store a decimal value for ship horizontal pos
		self.x = float(self.rect.x)

		#Movement flags
		self.moving_right = False
		self.moving_left = False
	def update(self):

		"""update the ship pos based on movement flag"""
		if self.moving_right:
			self.rect.x += 1
		if self.moving_left:
			self.rect.x -= 1

	def blitme(self):
		"""draw the ship in cur location"""
		self.screen.blit(self.image,self.rect)

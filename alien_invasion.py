import sys
import pygame

class AlienInvasion:
	"""overall class to manage game assets and behavior"""

	def __init__(self):
		"""init the game and create game resources"""
		#initializes the background settings needed for game to work
		pygame.init()

		#create a window using dimensiond from tuple (1200,800)
		# 1200 width, 800 height 
		#assigned to attribute self.screen so it can be available to everything in the class
		self.screen = pygame.display.set_mode((800,600))
		pygame.display.set_caption("Alien Invasion")

		#set background color
		self.bg_color = (230,230,230)


	def run_game(self):
		"""Start the main loop for the game"""
		while True:
			#poll for events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#redraw the screen during each pass through the loop
			self.screen.fill(self.bg_color)
			
			#make the most recenty drawn screen visible.
			pygame.display.flip()

if __name__ == '__main__':
	#make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
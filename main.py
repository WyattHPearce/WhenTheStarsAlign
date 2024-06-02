# Standard Imports
import sys
# Third-Party Imports
import pygame
# Local Imports
import globals as globals
import textures.texture_manager as texture_manager
# Scenes
import scenes.scene_manager as scene_manager
from scenes.level1 import Level1
from scenes.level2 import Level2

class Game:
    def __init__(self) -> None:
        pygame.init()

        # Create Screen
        self.screen: pygame.Surface = pygame.display.set_mode(
            (globals.screen_width, globals.screen_height), # Screen size
            pygame.RESIZABLE # Screen is resizable
        )

        # Initialize textures in texture manager
        texture_manager.init_textures()

        # Create clock
        self.clock = pygame.time.Clock()

        self.running: bool = True

        # Scenes
        scene_manager.set_state('level1')
        self.level1 = Level1(self)
        self.level2 = Level2(self)
        self.scenes = {
            'level1':self.level1,
            'level2':self.level2
        }

    def run(self) -> None:
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self) -> None:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Scene update
        self.scenes[scene_manager.get_state()].update()

        # Enforcing max framerate
        self.clock.tick(globals.max_framerate)
        # Updating the display
        pygame.display.update()

    def draw(self) -> None:
        # Scene draw
        self.scenes[scene_manager.get_state()].draw()

    def close(self) -> None:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
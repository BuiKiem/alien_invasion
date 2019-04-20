import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the ship's center property, not the rect.
        if self.moving_right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.centerx -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx

#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sep 2019
# This program draws a background on the PyBadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# a list of sprites
sprites = []

def main():
    # this function sets the background

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create sprite
    alien = stage.Sprite(image_bank_1, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 5, 75, 56)
    sprites.insert(0, ship)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + [background]
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    while True:
        # get user input

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    main()

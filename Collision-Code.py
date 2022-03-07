import math

def collision(player, ai_list):
    for ai in ai_list:
        if player.collides_with_sprite(ai):

            ai.change_x = - player.change_x * 2
            ai.change_y = - player.change_y * 2

        if player.collides_with_sprite(ai):

            player.change_x = - player.change_x * 2
            player.change_y = - player.change_y * 2
# Remember Use Pymunk. Much better collision

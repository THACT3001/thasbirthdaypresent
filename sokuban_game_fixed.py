import pygame
import sys
import os
from pygame.locals import *

width = 1000

height = 500

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

GREEN = (0, 255, 0)

ORANGE = (255, 140, 0)

display_surf = pygame.display.set_mode((width, height))

pygame.display.set_caption("Sokuban")

fps_clock = pygame.time.Clock()


class Player:

    def __init__(self, width, height, x, y):
        self.width = int(width)
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)
        self.dir_x = 0
        self.dir_y = 0

    def draw(self):
        pygame.draw.rect(display_surf, WHITE, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.dir_x * self.width
        self.y += self.dir_y * self.height
        self.dir_x = 0
        self.dir_y = 0


class Box:

    def __init__(self, width, height, x, y):
        self.width = int(width)
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)

    def draw(self):
        pygame.draw.rect(display_surf, WHITE, (self.x, self.y, self.width, self.height))

    def player_hit_box(self, player, boxes, walls):
        move_able = True
        if player.x == self.x - player.dir_x * width/20 and player.y == self.y:
            for box in boxes:
                if box.y == self.y and box.x == self.x + player.dir_x * width/20:
                    move_able = False
                    break
            if move_able:
                for wall in walls:
                    if wall.y == self.y and wall.x == self.x + player.dir_x * width/20:
                        move_able = False
                        break
            if move_able:
                self.x += player.dir_x * width/20
        elif player.y == self.y - player.dir_y * height/10 and player.x == self.x:
            for box in boxes:
                if box.x == self.x and box.y == self.y + player.dir_y * height/10:
                    move_able = False
                    break
            if move_able:
                for wall in walls:
                    if wall.x == self.x and wall.y == self.y + player.dir_y * height / 10:
                        move_able = False
                        break
            if move_able:
                self.y += player.dir_y * height/10
        return move_able

    def box_hit_destination(self, destinations):
        for destination in destinations:
            if destination.x == self.x and destination.y == self.y:
                return True
            else:
                return False


class Destination:

    def __init__(self, width, height, x, y):
        self.width = int(width)
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)

    def draw(self):
        pygame.draw.rect(display_surf, GREEN, (self.x, self.y, self.width, self.height))


class Wall:
    def __init__(self, width, height, x, y):
        self.width = int(width)
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)

    def draw(self):
        pygame.draw.rect(display_surf, ORANGE, (self.x, self.y, self.width, self.height))

    def wall_hit_player(self, player):
        if player.x + player.dir_x * player.width == self.x and player.y + player.dir_y * player.height == self.y:
            return True
        else:
            return False


class Game:

    def __init__(self, destinations, boxes, player, walls):
        self.destinations = destinations
        self.boxes = boxes
        self.player = player
        self.walls = walls

    def draw_arena(self):
        display_surf.fill(BLACK)
        for destination in self.destinations:
            destination.draw()
        for box in self.boxes:
            box.draw()
        self.player.draw()
        for wall in self.walls:
            wall.draw()

    def update(self):
        move_able = True
        for wall in self.walls:
            if wall.wall_hit_player(self.player):
                move_able = False
        if move_able:
            for box in self.boxes:
                move_able = box.player_hit_box(self.player, self.boxes, self.walls)
                if not move_able:
                    break
        if not move_able:
            self.player.dir_x = 0
            self.player.dir_y = 0
        self.player.move()


def main():
    pygame.init()

    wall1 = Wall(50, 50, 100, 0)
    wall2 = Wall(50, 50, 150, 0)
    wall3 = Wall(50, 50, 200, 0)
    wall4 = Wall(50, 50, 250, 0)
    wall5 = Wall(50, 50, 300, 0)
    wall6 = Wall(50, 50, 350, 0)
    wall7 = Wall(50, 50, 400, 0)
    wall8 = Wall(50, 50, 100, 50)
    wall9 = Wall(50, 50, 100, 100)
    wall10 = Wall(50, 50, 50, 100)
    wall11 = Wall(50, 50, 0, 100)
    wall12 = Wall(50, 50, 0, 150)
    wall13 = Wall(50, 50, 0, 200)
    wall14 = Wall(50, 50, 0, 250)
    wall15 = Wall(50, 50, 0, 300)
    wall16 = Wall(50, 50, 0, 350)
    wall17 = Wall(50, 50, 0, 400)
    wall18 = Wall(50, 50, 50, 400)
    wall19 = Wall(50, 50, 100, 400)
    wall20 = Wall(50, 50, 150, 400)
    wall21 = Wall(50, 50, 200, 400)
    wall22 = Wall(50, 50, 250, 400)
    wall23 = Wall(50, 50, 300, 400)
    wall24 = Wall(50, 50, 350, 400)
    wall25 = Wall(50, 50, 400, 400)
    wall26 = Wall(50, 50, 450, 400)
    wall27 = Wall(50, 50, 500, 400)
    wall28 = Wall(50, 50, 500, 350)
    wall29 = Wall(50, 50, 500, 300)
    wall30 = Wall(50, 50, 500, 250)
    wall31 = Wall(50, 50, 500, 200)
    wall32 = Wall(50, 50, 500, 150)
    wall33 = Wall(50, 50, 500, 100)
    wall34 = Wall(50, 50, 450, 100)
    wall35 = Wall(50, 50, 400, 100)
    wall36 = Wall(50, 50, 400, 50)
    wall37 = Wall(50, 50, 250, 50)
    wall38 = Wall(50, 50, 100, 200)
    wall39 = Wall(50, 50, 100, 250)
    wall40 = Wall(50, 50, 100, 300)
    wall41 = Wall(50, 50, 250, 250)
    wall42 = Wall(50, 50, 250, 300)
    wall43 = Wall(50, 50, 300, 300)
    wall44 = Wall(50, 50, 350, 300)
    wall45 = Wall(50, 50, 400, 300)
    wall46 = Wall(50, 50, 400, 250)
    wall47 = Wall(50, 50, 400, 200)

    box1 = Box(50, 50, 150, 100)
    box2 = Box(50, 50, 150, 150)
    box3 = Box(50, 50, 150, 200)
    box4 = Box(50, 50, 350, 100)
    box5 = Box(50, 50, 350, 150)
    box6 = Box(50, 50, 350, 200)
    box7 = Box(50, 50, 150, 300)
    box8 = Box(50, 50, 200, 300)

    destination1 = Destination(50, 50, 200, 100)
    destination2 = Destination(50, 50, 250, 100)
    destination3 = Destination(50, 50, 300, 100)
    destination4 = Destination(50, 50, 200, 150)
    destination5 = Destination(50, 50, 200, 200)
    destination6 = Destination(50, 50, 250, 200)
    destination7 = Destination(50, 50, 300, 200)
    destination8 = Destination(50, 50, 300, 150)

    player = Player(50, 50, 50, 200)

    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14]
    boxes = [box1, box2, box3, box4, box5, box6, box7, box8]
    destinations = [destination1, destination2, destination3, destination4, destination5, destination6, destination7]

    walls.append(wall15)
    walls.append(wall16)
    walls.append(wall17)
    walls.append(wall18)
    walls.append(wall19)
    walls.append(wall20)
    walls.append(wall21)
    walls.append(wall22)
    walls.append(wall23)
    walls.append(wall24)
    walls.append(wall25)
    walls.append(wall26)
    walls.append(wall27)
    walls.append(wall28)
    walls.append(wall29)
    walls.append(wall30)
    walls.append(wall31)
    walls.append(wall32)
    walls.append(wall33)
    walls.append(wall34)
    walls.append(wall35)
    walls.append(wall36)
    walls.append(wall37)
    walls.append(wall38)
    walls.append(wall39)
    walls.append(wall40)
    walls.append(wall41)
    walls.append(wall42)
    walls.append(wall43)
    walls.append(wall44)
    walls.append(wall45)
    walls.append(wall46)
    walls.append(wall47)

    destinations.append(destination8)

    game = Game(destinations, boxes, player, walls)

    win = False

    while True:
        fps = 20

        for box in boxes:
            if box.box_hit_destination(destinations):
                win = True
            else:
                win = False
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_w:
                player.dir_x = 0
                player.dir_y = -1
            elif event.type == KEYDOWN and event.key == K_s:
                player.dir_x = 0
                player.dir_y = 1
            elif event.type == KEYDOWN and event.key == K_d:
                player.dir_x = 1
                player.dir_y = 0
            elif event.type == KEYDOWN and event.key == K_a:
                player.dir_x = -1
                player.dir_y = 0

            game.draw_arena()
            game.update()
            pygame.display.update()
            fps_clock.tick(fps)

            if win:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
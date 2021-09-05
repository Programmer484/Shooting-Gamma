import pygame
import time
from os import path

pygame.init()
pygame.mixer.init()
#Creates a path that just makes it easier to access files(instead of typing smtg like 'c://user/desktop/pygame/image.png')
#path.dirname(__file__) gets the parent directory of wherever the image resides(e.g c://user/desktop/pygame)
img_dir = path.join('img')


#REMEMBER to make the 'workspace' big enough so you can see the entire game window, or else the player will be cut off.
class Game():
    def __init__(self, imagelist, width, height):
        #Screen size variables    
        self.width = width
        self.height = height
        #Creating the window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Shooting Gamma')
        #Arena the players will play in
        self.arena = 0
        #Determines what screen to show(E.g setup, menu, Game over, etc)
        self.screen = 'play'
        #List of images for background
        self.imagelist = imagelist
        #Takes image out of imagelist according to self.arena value
        self.image = pygame.transform.scale(self.imagelist[self.arena],
                                            (self.width, self.height))
        #Gets rectangle with the dimensions of the image 
        self.image_rect = self.image.get_rect()
        #Clock for determing how quickly the frames update
        self.clock = pygame.time.Clock()
        self.FPS = 60
        pygame.key.set_repeat(60)
        #Restart variable is for determining whether or not the player wants to restart the game
        self.running = True
        self.restart = True
        self.winner = None
        

    def update(self):
        #Draw background
        self.window.blit(self.image, self.image_rect)


    #Sets platform positions based on self.arena value
    def reset(self):
        if self.arena == 0:
            p1 = Obstacle(platform1, 50, 200)
            p2 = Obstacle(platform1, 125, 250)
            p3 = Obstacle(platform1, 200, 300)
        elif self.arena == 1:
            p1 = Obstacle(platform1, 150, 200)
            p2 = Obstacle(platform1, 225, 250)
            p3 = Obstacle(platform1, 300, 300)

    def mainloop(self):
        while True:
            getinputs = input()
            if 'RETURN' in getinputs:
                pygame.quit()
                break
            if self.screen == 'setup':
                #Player 1
                Left1 = button(self.window, (390, 300), "Left")
                Right1 = button(self.window, (490, 300), "Right")
                Jump1 = button(self.window, (440, 240), "Jump")
                #Block1 = button(self.window, (440, 240), "Block")
                #Shoot1 = button(self.window, (440, 240), "Shoot")
                #Player 2
                Left2 = button(self.window, (90, 300), "Left")
                Right2 = button(self.window, (190, 300), "Right")
                Jump2 = button(self.window, (140, 240), "Jump")
                #Block2 = button(self.window, (440, 240), "Block")
                #Shoot2 = button(self.window, (440, 240), "Shoot")

                start = button(self.window, (0, 0), "Start")
                #Sorry for the inefficiencyyy
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Left1.collidepoint(pygame.mouse.get_pos()):
                            k = keyselect()
                            player1.left = k
                        elif Right1.collidepoint(pygame.mouse.get_pos()):
                            k = keyselect()
                            player1.right = k
                        elif Jump1.collidepoint(pygame.mouse.get_pos()):
                            k = keyselect()
                            player1.jump = k
                        #elif Block1.collidepoint(pygame.mouse.get_pos()):
                        #    k = keyselect()
                        #elif Shoot1.collidepoint(pygame.mouse.get_pos()):
                            k = keyselect()

                        elif Left2.collidepoint(pygame.mouse.get_pos()):
                            k = keyselect()
                            #player2.left = k
                        elif Right2.collidepoint(pygame.mouse.get_pos()):
                            k = keyselect()
                            #player2.right = k
                        elif Jump2.collidepoint(pygame.mouse.get_pos()):
                            k = keyselect()
                            #player2.jump = k
                        #elif Block2.collidepoint(pygame.mouse.get_pos()):
                        #    k = keyselect()
                        #elif Shoot2.collidepoint(pygame.mouse.get_pos()):
                        #    k = keyselect()
                        elif start.collidepoint(pygame.mouse.get_pos()):
                            self.screen = 'play'

            elif self.screen == 'menu':
                print('''You hacked the code. The menu doesn't even exist''')

            elif self.screen == 'play':
                if self.restart == True:
                    self.reset()
                    self.restart = False
                self.update()
                all_sprites.update()
                all_sprites.draw(self.window)
                if player1.hitpoints <= 0:
                    self.screen = 'endgame'
                    self.winner = 'player2'
                #elif player2.hitpoints == 0:
                #  self.screen = 'endgame'
                #  self.winner = 'player1'

            elif self.screen == 'endgame':
                #Just so we can access this from outside the Game Class
                display1 = pygame.display.get_surface()
                widthcenter = display1.get_width() / 2
                heightcenter = display1.get_height() / 2
                pygame.display.set_mode(
                    (display1.get_width(), display1.get_height()))
                button(self.window, ((widthcenter - 140, heightcenter - 100)),
                       "GAME OVER")
                if self.winner == "player1":
                    button(self.window, (widthcenter - 140, heightcenter),
                           "Player 1 Wins")
                else:
                    button(self.window, (widthcenter - 140, heightcenter),
                           "Player 2 Wins")
                restart = button(
                    self.window,
                    (widthcenter - 100, display1.get_height() - 60), "RESTART")
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart.collidepoint(pygame.mouse.get_pos()):
                            self.screen = 'setup'
                            pygame.display.set_mode(
                                (display1.get_width(), display1.get_height()))

            pygame.display.flip()
            self.clock.tick(self.FPS)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_sprites.add(self)
        obstacles.add(self)

    def update(self):
        #pygame.draw.rect(
        #    Arena.window, (0, 255, 255),
        #    (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        pass



class Block(Obstacle):
    def __init__(self, image, x, y, width = 20, height = 40, hitpoints = 100):
        Obstacle.__init__(self, image, x, y)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.hitpoints = hitpoints

    def update(self):
        for projectile in projectiles:
          if pygame.Rect.colliderect(projectile.rect, self.rect):
            self.hitpoints += projectile.damage
        if self.hitpoints < 0:
          self.kill()
class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.rect.width
        self.height = self.rect.height
        #Movement speed + direction
        self.speed = None
        self.speedx = 0
        self.speedy = 0
        #Damage and Health
        self.hitpoints = 100
        self.alive = True
        #Default values for player ctrls.
        self.left = pygame.K_LEFT
        self.right = pygame.K_RIGHT
        self.block = pygame.K_DOWN
        self.jump = pygame.K_SPACE
        self.shoot = pygame.K_0
        self.shooting = True
        #Jump variables
        self.jumpCount = 0
        
        self.canJump = True
        self.gravity = 10
        #Block placement variables
        self.blockCount = 0
        self.maxblock = 10
        self.blockready = 0
        #Shooting variables
        #-1 = facing left, 1 = facing right
        self.facing = 1
        self.shooting = False

        all_sprites.add(self)
        players.add(self)

    def update(self):
        #pygame.draw.rect(
        #    Arena.window, (0, 255, 255),
        #    (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        self.speedx = 0
        self.shooting = False
        k = pygame.key.get_pressed()
        if k[self.left]:
            self.facing = -1
            self.speedx = -5
            if self.rect.left + self.speedx <= 0:
                self.speedx = 0
                self.rect.left = 0

        if k[self.right]:
            self.facing = 1
            self.speedx = 5
            if self.rect.right + self.speedx >= Arena.width:
                self.speedx = 0
                self.rect.right = Arena.width

        if k[self.jump]:
            if self.canJump == True:
                self.jumpCount = 10
                self.canJump = False

        if k[self.shoot]:
            #In the Gun class we can make its update constantly check if the player's shooting variable is True
            self.shooting = True

        if k[self.block] and self.blockready > 10:
            if self.blockCount < self.maxblock:
                self.blockCount += 1
                self.blockready = 0
                b = Block(
                    block1,
                    self.rect.centerx + self.facing * (self.width/2 + 10),
                    self.rect.bottom - 40)

                obstacles.add(b)
                all_sprites.add(b)

        #Recharge for placing blocks
        self.blockready += 1

        if self.jumpCount > 0:
            self.speedy = -(self.jumpCount * self.jumpCount) * 0.2
            self.jumpCount -= 1
        else:
            self.speedy = self.gravity
        self.Collisions()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def Collisions(self):
        if self.rect.bottom + self.speedy >= Arena.height:
            self.speedy = 0
            self.rect.bottom = Arena.height
            self.canJump = True
        elif self.rect.top - self.speedy < 0:
            self.jumpCount = 0
            self.rect.top = 0
            self.canJump = False

        for o in obstacles:
            if collide_bottom(self, o) and self.jumpCount == 0:
                if o.rect.top - self.rect.bottom >= 0:
                    self.speedy = o.rect.top - self.rect.bottom
                else:
                    self.rect.bottom = o.rect.top
                    self.speedy = 0
                self.canJump = True

            if collide_top(self, o):
                if o.rect.bottom - self.rect.top <= 0:
                    self.speedy = o.rect.bottom - self.rect.top
                else:
                    self.rect.top = o.rect.bottom
                    self.speedy = self.gravity
                self.canJump = False

            if collide_left(self, o):
                if o.rect.right - self.rect.left <= 0:
                    self.speedx = o.rect.right - self.rect.left

            if collide_right(self, o):
                if o.rect.left - self.rect.right >= 0:
                    self.speedx = o.rect.left - self.rect.right

#I'm thinking we should have a Gun Class, so we can make different types of guns later on.


class Gun(pygame.sprite.Sprite):
    def __init__(self, player, width, height, costume, firerate):
        pygame.sprite.Sprite.__init__(self)
        img = costume
        self.image = pygame.transform.scale(img, (width, height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.player = player
        #self.facing = self.player.facing
        self.firerate = firerate
        self.firerateClock = self.firerate
        self.player = player
        
        guns.add(self)
        all_sprites.add(self)

    def update(self):
      #Gun position in relation to player. Ignore the direction it's currently facing.
        self.facing = self.player.facing
        self.rect.centerx = self.player.rect.centerx + self.facing * (self.player.rect.width/2 + 25)
        self.rect.centery = self.player.rect.centery


        if self.player.shooting == True and self.firerateClock == 0:
            if self.facing == 1:
              print('shoot')
            else:
              print('why did you shoot yourself?')
            self.firerateClock = self.firerate
        if self.firerateClock > 0:
            self.firerateClock -= 1


class Projectile(Gun):
    def __init__(self, radius):
        pygame.sprite.Sprite.__init__(self)
        projectiles.add(self)
        all_sprites.add(self)


#INPUT FUNCTION
def input():
    toreturn = []
    for event in pygame.event.get():
        pressedkeys = pygame.key.get_pressed()
        shift = pressedkeys[pygame.K_LSHIFT] or pressedkeys[pygame.K_RSHIFT]
        ctrl = pressedkeys[pygame.K_LCTRL] or pressedkeys[pygame.K_RCTRL]
        alt = pressedkeys[pygame.K_LALT] or pressedkeys[pygame.K_RALT]

        if event.type == pygame.QUIT:
            toreturn.append("RETURN")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                toreturn.append("UP")
            if event.key == pygame.K_DOWN:
                toreturn.append("DOWN")
            if event.key == pygame.K_LEFT:
                toreturn.append("LEFT")
            if event.key == pygame.K_RIGHT:
                toreturn.append("RIGHT")
            if event.key == pygame.K_SPACE:
                toreturn.append("JUMP")

            if event.key == pygame.K_F4 and alt:
                toreturn.append("RETURN")
            if event.key == pygame.K_q and ctrl:
                toreturn.append("RETURN")
            if event.key == pygame.K_ESCAPE:
                toreturn.append("RETURN")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousexy = pygame.mouse.get_pos()
            x = mousexy[0]
            y = mousexy[1]
            toreturn.append(["MOUSE", x, y])
    #print(toreturn)
    return toreturn


def keyselect():
    b = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
                print(key)
                b = True
        if b:
            break
    return key


#Collision detection
#
#
def within_x(object1, object2):
    #Returns whether a given object is overlapping with player sprite.
    if (object1.rect.right > object2.rect.left and object1.rect.right < object2.rect.right)\
        or (object1.rect.left > object2.rect.left and object1.rect.left < object2.rect.right)\
        or (object2.rect.right > object1.rect.left and object2.rect.right < object1.rect.right)\
        or (object2.rect.left > object1.rect.left and object2.rect.left < object1.rect.right):
        return True
    return False


def within_y(object1, object2):
    #Returns whether a given object is overlapping with player sprite.
    if (object1.rect.bottom > object2.rect.top and object1.rect.bottom < object2.rect.bottom)\
        or (object1.rect.top > object2.rect.top and object1.rect.top < object2.rect.bottom)\
        or (object2.rect.bottom > object1.rect.top and object2.rect.bottom < object1.rect.bottom)\
        or (object2.rect.top > object1.rect.top and object2.rect.top < object1.rect.bottom):
        return True
    return False


def collide_left(object1, object2):
    if within_y(object1, object2):
        x_calc = object1.rect.left + object1.speedx
        if x_calc <= object2.rect.right and x_calc >= object2.rect.left:
            return True
    return False


def collide_right(object1, object2):
    if within_y(object1, object2):
        x_calc = object1.rect.right + object1.speedx
        if x_calc >= object2.rect.left and x_calc <= object2.rect.right:
            return True
    return False


def collide_top(object1, object2):
    if within_x(object1, object2):
        y_calc = object1.rect.top + object1.speedy
        if y_calc <= object2.rect.bottom and object1.rect.top >= object2.rect.top:
            return True
    return False


def collide_bottom(object1, object2):
    if within_x(object1, object2):
        y_calc = object1.rect.bottom + object1.gravity
        if y_calc >= object2.rect.top and object1.rect.bottom <= object2.rect.bottom:
            return True
    return False


#Totally did not copy code from elsewhere.
def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
    return screen.blit(text_render, (x, y))


background = pygame.image.load(path.join(img_dir, "background.png"))
images = [background, background]
Arena = Game(images, 600, 400)

#Game Pictures

platform1 = pygame.image.load(path.join(img_dir, "platform1.png")).convert()
player = pygame.image.load(path.join(img_dir, "player.png")).convert()
block1 = pygame.image.load(path.join(img_dir, "block.png")).convert()
gun = pygame.image.load(path.join(img_dir, "gun.png")).convert_alpha()

#Makes a group we can put sprites in.
obstacles = pygame.sprite.Group()
players = pygame.sprite.Group()
guns = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player1 = Player(player, 100, 300, 40, 60)
player2 = Player(block1, 200, 100, 40, 60)
gun1 = Gun(player1, 40, 20, gun, Arena.FPS/2)

Arena.mainloop()

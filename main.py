import pygame
from pygame.locals import *
import os
import random as R

showhitboxes = False
sound = True
howto = True

pygame.init()
pygame.mixer.init()

W, H = 850, 445  # these are the measurements of the bg.png file
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("peep")

bg = pygame.image.load(os.path.join("images", "bg.png")).convert()
bgX = 0
bgX2 = bg.get_width()
gameicon = pygame.image.load(os.path.join("images", "icon.png"))
pygame.display.set_icon(gameicon)

clock = pygame.time.Clock()


class player(object):  # tim
    run = [
        pygame.image.load(os.path.join("images", str(x) + ".png")) for x in range(8, 16)
    ]
    jump = [
        pygame.image.load(os.path.join("images", str(x) + ".png")) for x in range(1, 8)
    ]
    slide = [
        pygame.image.load(os.path.join("images", "S1.png")),
        pygame.image.load(os.path.join("images", "S2.png")),
        pygame.image.load(os.path.join("images", "S2.png")),
        pygame.image.load(os.path.join("images", "S2.png")),
        pygame.image.load(os.path.join("images", "S2.png")),
        pygame.image.load(os.path.join("images", "S2.png")),
        pygame.image.load(os.path.join("images", "S2.png")),
        pygame.image.load(os.path.join("images", "S2.png")),
        pygame.image.load(os.path.join("images", "S3.png")),
        pygame.image.load(os.path.join("images", "S4.png")),
        pygame.image.load(os.path.join("images", "S5.png")),
    ]
    fall = pygame.image.load(os.path.join("images", "0.png"))
    jumpList = [
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -2,
        -2,
        -2,
        -2,
        -2,
        -2,
        -2,
        -2,
        -2,
        -2,
        -2,
        -2,
        -3,
        -3,
        -3,
        -3,
        -3,
        -3,
        -3,
        -3,
        -3,
        -3,
        -3,
        -3,
        -4,
        -4,
        -4,
        -4,
        -4,
        -4,
        -4,
        -4,
        -4,
        -4,
        -4,
        -4,
    ]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 30))
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            win.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (
                self.x + 4,
                self.y,
                self.width - 24,
                self.height - 10,
            )  # hitbox time
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            elif (
                self.slideCount > 20 and self.slideCount < 80
            ):  # checks if it is sliding or not
                self.hitbox = (
                    self.x,
                    self.y + 3,
                    self.width - 8,
                    self.height - 35,
                )  # changes the hitbox for slidding

            if self.slideCount >= 110:
                self.slideCount = 0
                self.runCount = 0
                self.slideUp = False
                self.hitbox = (
                    self.x + 4,
                    self.y,
                    self.width - 24,
                    self.height - 10,
                )  # same as 48
            win.blit(self.slide[self.slideCount // 10], (self.x, self.y))
            self.slideCount += 1

        else:
            # this says the player is just running and animates as so
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount // 6], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 13)

        if showhitboxes == True:
            pygame.draw.rect(
                win, (255, 0, 0), self.hitbox, 2
            )  #  review the player hitbox


# end of the swiped/edited player class code


class saw(object):
    rotate = [
        pygame.image.load(os.path.join("images", "SAW0.png")),
        pygame.image.load(os.path.join("images", "SAW1.png")),
        pygame.image.load(os.path.join("images", "SAW2.png")),
        pygame.image.load(os.path.join("images", "SAW3.png")),
    ]  # saw animation

    def __init__(self, x, y, width, height):  # sets inital attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self, win):  # how/where the hitbox and the saw is made
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        if showhitboxes == True:
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.rotateCount >= 8:
            self.rotateCount = 0
        win.blit(
            pygame.transform.scale(self.rotate[self.rotateCount // 2], (64, 64)),
            (self.x, self.y),
        )  # makes and resizes the saw img
        self.rotateCount += 1

    def collide(self, rect):
        if (
            rect[0] + rect[2] > self.hitbox[0]
            and rect[0] < self.hitbox[0] + self.hitbox[2]
        ):  # checks if X is hit
            if rect[1] + rect[3] > self.hitbox[1]:  # checks Y
                return True
        return False


class bird(object):
    fly = [
        pygame.image.load(os.path.join("images", "B1.png")),
        pygame.image.load(os.path.join("images", "B2.png")),
        pygame.image.load(os.path.join("images", "B3.png")),
        pygame.image.load(os.path.join("images", "B4.png")),
        pygame.image.load(os.path.join("images", "B1.png")),
        pygame.image.load(os.path.join("images", "B2.png")),
        pygame.image.load(os.path.join("images", "B3.png")),
        pygame.image.load(os.path.join("images", "B4.png")),
    ]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.flyCount = 0
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 20, self.y + 1, self.width - 20, self.height - 10)
        if showhitboxes == True:
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.flyCount >= 8:
            self.flyCount = 0
        win.blit(
            pygame.transform.scale(self.fly[self.flyCount // 2], (72, 64)),
            (self.x, self.y),
        )
        self.flyCount += 1

    def collide(self, rect):
        if (
            rect[0] + rect[2] > self.hitbox[0]
            and rect[0] < self.hitbox[0] + self.hitbox[2]
        ):  # checks if X is hit
            if 315 > character.hitbox[1]:  # checks Y
                return True
        return False


class red(object):
    run = [
        pygame.image.load(os.path.join("images", "R1.png")),
        pygame.image.load(os.path.join("images", "R2.png")),
        pygame.image.load(os.path.join("images", "R3.png")),
        pygame.image.load(os.path.join("images", "R4.png")),
        pygame.image.load(os.path.join("images", "R5.png")),
        pygame.image.load(os.path.join("images", "R6.png")),
        pygame.image.load(os.path.join("images", "R1.png")),
        pygame.image.load(os.path.join("images", "R2.png")),
        pygame.image.load(os.path.join("images", "R3.png")),
        pygame.image.load(os.path.join("images", "R4.png")),
        pygame.image.load(os.path.join("images", "R5.png")),
        pygame.image.load(os.path.join("images", "R6.png")),
    ]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.runCount = 0
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 25, self.width - 20, self.height - 25)
        if showhitboxes == True:
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.runCount >= 12:
            self.runCount = 0
        win.blit(
            pygame.transform.scale(self.run[self.runCount // 2], (64, 64)),
            (self.x, self.y),
        )
        self.runCount += 1

    def collide(self, rect):
        if (
            rect[0] + rect[2] > self.hitbox[0]
            and rect[0] < self.hitbox[0] + self.hitbox[2]
        ):  # checks if X is hit
            if rect[1] + rect[3] > self.hitbox[1]:  # checks Y
                return True
        return False


class blue(object):
    run = [
        pygame.image.load(os.path.join("images", "BL1.png")),
        pygame.image.load(os.path.join("images", "BL2.png")),
        pygame.image.load(os.path.join("images", "BL3.png")),
        pygame.image.load(os.path.join("images", "BL4.png")),
        pygame.image.load(os.path.join("images", "BL5.png")),
        pygame.image.load(os.path.join("images", "BL6.png")),
        pygame.image.load(os.path.join("images", "BL1.png")),
        pygame.image.load(os.path.join("images", "BL2.png")),
        pygame.image.load(os.path.join("images", "BL3.png")),
        pygame.image.load(os.path.join("images", "BL4.png")),
        pygame.image.load(os.path.join("images", "BL5.png")),
        pygame.image.load(os.path.join("images", "BL6.png")),
    ]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.runCount = 0
        self.vel = 1.4

    def draw(self, win):
        self.hitbox = (self.x + 20, self.y + 5, self.width - 20, self.height + 10)
        if showhitboxes == True:
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.runCount >= 12:
            self.runCount = 0
        win.blit(
            pygame.transform.scale(self.run[self.runCount // 2], (64, 64)),
            (self.x, self.y),
        )
        self.runCount += 1

    def collide(self, rect):
        if (
            rect[0] + rect[2] > self.hitbox[0]
            and rect[0] < self.hitbox[0] + self.hitbox[2]
        ):  # checks if X is hit
            if rect[1] + rect[3] > self.hitbox[1]:  # checks Y
                return True
        return False


def fileupdate():
    f = open("scores.txt", "r")  # opens the file in the read mode
    file = f.readlines()
    last = int(file[0])  # first line

    if last < int(score):
        f.close()
        file = open("scores.txt", "w")  # opens the file in the write mode
        file.write(str(score))
        file.close()

        return score

    return last


def endscreen():  # triggers when died
    global pause, score, speed, obstacles, alreadydead  # refers to the big ones
    pause = 0
    speed = 60
    obstacles = []
    tempbg = pygame.image.load(os.path.join("images", "Untitled.png")).convert()
    run = True
    while run:  # makes a new temp loop to run in
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if (
                event.type == pygame.MOUSEBUTTONDOWN
            ):  # do nothing till a mouse button is pressed
                run = False
                character.falling = False
                character.sliding = False
                character.jumpin = False
                alreadydead = False

        win.blit(tempbg, (0, 0))  # reset bg
        largeFont = pygame.font.SysFont(
            "comicsans", 80
        )  # feedback on the ending screen
        smallFont = pygame.font.SysFont("comicsans", 55)
        lastscore = largeFont.render(
            "Best Score: " + str(fileupdate()), 1, (255, 255, 255)
        )
        currentscore = largeFont.render("Score: " + str(score), 1, (255, 255, 255))
        mouse = smallFont.render("Press any mouse button to retry!", 1, (255, 255, 255))

        win.blit(lastscore, (W / 2 - lastscore.get_width() / 2, 120))
        win.blit(currentscore, (W / 2 - currentscore.get_width() / 2 + 120, 240))
        win.blit(mouse, (W / 2 - mouse.get_width() / 2, 395))
        # makes the text stay in the middle ish no mattr the size/alters
        pygame.display.update()
    score = 0


def redrawWindow():  # this will be where ALL on screen changes will be made
    largeFont = pygame.font.SysFont("comicsans", 30)
    smallFont = pygame.font.SysFont("comicsans", 25)
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))

    text = largeFont.render("Score: " + str(score), 1, (255, 255, 255))

    if howto == True:
        instructions = smallFont.render(
            "Use the arrow keys to jump and slide in order", 1, (255, 255, 255)
        )
        instructions2 = smallFont.render(
            "to get past the obstacles in your way! (Hide this with Z)",
            1,
            (255, 255, 255),
        )
        win.blit(instructions, (10, 390))
        win.blit(instructions2, (10, 410))
    if sound == True:
        soundtext = largeFont.render("Sound is On! (S)", 1, (255, 255, 255))
    if sound == False:
        soundtext = largeFont.render("Sound is Off! (S)", 1, (255, 255, 255))
    if showhitboxes == True:
        hitboxtext = largeFont.render("Hit boxes are Shown! (X)", 1, (255, 255, 255))
    if showhitboxes == False:
        hitboxtext = largeFont.render("Hit boxes are Hidden! (X)", 1, (255, 255, 255))

    character.draw(win)  # makes the character appear
    for obstacle in obstacles:  # draw stuff from the objects list
        obstacle.draw(win)

    win.blit(text, (700, 10))
    win.blit(soundtext, (10, 10))
    win.blit(hitboxtext, (10, 40))

    pygame.display.update()


pygame.time.set_timer(USEREVENT + 1, 500)
pygame.time.set_timer(USEREVENT + 2, 3000)

speed = 30
score = 0
run = True
character = player(200, 313, 64, 64)
obstacles = []
pause = 0
fallSpeed = 0
alreadydead = False

songlist = [
    (os.path.join("sounds", "peepo.mp3")),
    (os.path.join("sounds", "peepo.mp3")),
]
jump_effect = pygame.mixer.Sound(os.path.join("sounds", "jump.wav"))  # sound start up
slide_effect = pygame.mixer.Sound(os.path.join("sounds", "slide.wav"))
death_effect = pygame.mixer.Sound(os.path.join("sounds", "death.wav"))

pygame.mixer.music.load(R.choice(songlist))
pygame.mixer.music.play(-1)

while run:
    if pause > 0:  # if u ded
        pause += 1
        if pause > fallSpeed * 2:  # ensures fps stays constant as fall*2 = 2 seconds
            endscreen()

    score = speed // 10 - 6  # makes it 0 cuz stonks

    for obstacle in obstacles:  # slides objs
        if obstacle.collide(character.hitbox):
            character.falling = True
            if sound == True:
                if alreadydead == False:
                    death_effect.play()
                    alreadydead == True
            if pause == 0:  # makes sure you didnt die already
                pause = 1  # stops this from running again before a restart
                fallSpeed = speed  # syncs to fps
        if obstacle.x < -64:  # finds the saws location
            obstacles.pop(obstacles.index(obstacle))  # delete if gone
        else:
            obstacle.x -= 1.4

    bgX -= 1.4  # moves the bg by 1.4px based on the clocks tick speed
    bgX2 -= 1.4

    if (
        bgX < bg.get_width() * -1
    ):  # if the background is 100px long and is at -100 we need to restart the image on the other side
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for (
        event
    ) in pygame.event.get():  # this is the exit handler for when you exit the window
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        if event.type == USEREVENT + 1:
            speed += 1

        if event.type == USEREVENT + 2:  # the trigger for a obstickale to spawn
            r = R.randrange(0, 5)
            if r == 0:
                obstacles.append(saw(810, 310, 64, 64))
            if r == 1:
                obstacles.append(bird(810, 265, 64, 64))
            if r == 2:
                obstacles.append(red(810, 310, 64, 64))
            if r == 3:
                obstacles.append(blue(810, 310, 64, 64))
            elif r == 4:
                pass

    if character.falling == False:
        keys = pygame.key.get_pressed()  # makes key reg ez use[] to get in ()

        if (
            keys[pygame.K_SPACE] or keys[pygame.K_UP]
        ):  # if you push down it runs the jump event
            if not (character.jumping):  # makes sure you arent jump
                character.jumping = True  # jump time
                if sound == True:
                    jump_effect.play()

        if keys[pygame.K_DOWN]:  # same as jump but slid this time
            if not (character.sliding):
                character.sliding = True
                if sound == True:
                    slide_effect.play()

        if keys[pygame.K_x]:
            if showhitboxes == True:
                showhitboxes = False
            else:
                showhitboxes = True

        if keys[pygame.K_s]:
            if sound == True:
                sound = False
                pygame.mixer.music.pause()
            else:
                sound = True
                pygame.mixer.music.unpause()

        if keys[pygame.K_z]:
            if howto == True:
                howto = False
            else:
                howto = True

    clock.tick(speed)
    redrawWindow()

import pygame
import os
import random


pygame.init()

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    image.set_colorkey(GREEN)
    return(image)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

nn = 0
f = open("hi_score_dino.txt", encoding="cp1251")
lines = f.read()
HI_SCORE = int(lines)
f.close()

running_sprite = True
pos_p = 1700
pos_k = 1200
score = 0
size = width, height = [1200, 800]
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
dino_and_kaktus = pygame.sprite.Group()

class Dino(pygame.sprite.Sprite):
    image0 = load_image("step0.png")
    image1 = load_image("step1.png")
    image2 = load_image("step2.png")
    image3 = load_image("lie1.png")
    image4 = load_image("lie2.png")

    def __init__(self, group):
        super().__init__(group)
        self.speed = 25
        self.st = 0
        self.ll = 0
        self.image = Dino.image0
        self.rect = self.image.get_rect()
        self.rect.x = 60
        self.rect.y = 600
        self.I = 0
        self.die = 1
        self.n = 0
        self.O = 0
        self.lie = 0
        self.li = 0
        self.ttt = 0

    def update(self, args, *p):
        global running_sprite
        global score
        blocks_hit_list = pygame.sprite.spritecollide(self, dino_and_kaktus, False)
        if len(blocks_hit_list) > 1:
            self.n += 1
            running_sprite = False
            if self.n == 1:
                self.speed = 25

        if running_sprite == True:
            self.st += 1
            if self.st == 21:
                self.st = 1
                score += 1
            if self.O == 0:
                if self.ttt == 1:
                    self.rect.y = 600
                    self.st = 5
                    self.ttt = 0
                if self.st == 5:
                    self.image = Dino.image0
                if self.st == 10:
                    self.image = Dino.image1
                if self.st == 15:
                    self.image = Dino.image0
                if self.st == 20:
                    self.image = Dino.image2
            elif self.O == 1:
                if 0 < self.st < 11:
                    self.lie += 1
                    if self.lie == 1:
                        self.rect.y = 633
                        self.image = Dino.image4
                elif 10 < self.st < 21:
                    self.lie += 1
                    if self.lie == 1:
                        self.rect.y = 633
                        self.image = Dino.image3
                if self.st == 10:
                    self.image = Dino.image3
                if self.st == 20:
                    self.image = Dino.image4
            
            
            if x == 1 and y == 0:
                self.I = 1
                
            if y == 1 and self.I == 0:
                self.lie = 0
                self.O = 1
                self.li = 0
                
            if y == 0:
                self.li += 1
                if self.li == 1:
                    self.O = 0
                    self.ttt = 1
            
            if self.I == 1:
                if self.st % 1 == 0:
                    self.rect.y -= self.speed
                    if self.rect.y == 600:
                        self.I = 2
                    self.speed -= 1
                if self.I == 2:
                    self.I = 0
                    self.speed = 25
            
        else:
            if self.st % 1 == 0 and self.die == 1:
                self.rect.y -= self.speed
                if self.rect.y > 900:
                    self.die = 0
                self.speed -= 1

                

class Grass1(pygame.sprite.Sprite):
    image = load_image("ground.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = Grass1.image
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 686
        

    def update(self, args):
        if running_sprite == True:
            self.rect.x -= 10
            if self.rect.x == -1200:
                self.rect.x = 1200


class Grass2(pygame.sprite.Sprite):
    image = load_image("ground.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = Grass2.image
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 686
        

    def update(self, args):
        if running_sprite == True:
            self.rect.x -= 10
            if self.rect.x == -1200:
                self.rect.x = 1200


class Kaktus1(pygame.sprite.Sprite):
    image = load_image("kaktus2.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = Kaktus1.image
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 600
        self.x1 = 1200

    def update(self, args):
        global pos_k
        global nn
        if running_sprite == True:
            pos_k = self.rect.x
            self.rect.x -= 10
            if self.rect.x < -100 and pos_p < 1200:
                self.rect.x = random.randrange(1300, 1800, 100)
            elif self.rect.x < -100 and pos_p > 1200:
                self.rect.x = pos_p + random.randrange(500, 1000, 100)
            
            if args.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args.pos):
                self.kill()
                nn += 1


class Cloud1(pygame.sprite.Sprite):
    image = load_image("cloud.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = Cloud1.image
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1250
        self.rect.y = 200
        

    def update(self, args):
        if running_sprite == True:
            self.rect.x -= 2
            if self.rect.x == -100:
                self.rect.x = 1250


class Cloud2(pygame.sprite.Sprite):
    image = load_image("cloud.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = Cloud2.image
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 170
        

    def update(self, args):
        if running_sprite == True:
            self.rect.x -= 2
            if self.rect.x == -100:
                self.rect.x = 1250


class Pterodactel(pygame.sprite.Sprite):
    image1 = load_image("pte1.png")
    image2 = load_image("pte2.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = Pterodactel.image1
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 1700
        self.rect.y = 550
        self.t = 0
    


    def update(self, args):
        global nn
        global pos_p
        if running_sprite == True:
            pos_p = self.rect.x
            self.st += 1
            if self.st == 21:
                self.st = 1
            
            if self.st == 10 and self.t % 2 == 0:
                self.image = Pterodactel.image1
                self.t += 1
            elif self.st == 10 and self.t % 2 != 0:
                self.image = Pterodactel.image2
                self.t += 1
                
                
            self.rect.x -= 10
            if self.rect.x < -100 and pos_k < 1200:
                self.rect.x = random.randrange(1300, 1800, 100)
            elif self.rect.x < -100 and pos_k > 1200:
                self.rect.x = pos_k + random.randrange(500, 1000, 100)
            
            if args.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args.pos):
                self.kill()
                nn += 1


class Pterodactel2(pygame.sprite.Sprite):
    image1 = load_image("pte1.png")
    image2 = load_image("pte2.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = Pterodactel2.image1
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 2200
        self.rect.y = 400
        self.t = 0
    


    def update(self, args):
        global nn
        if running_sprite == True:
            self.st += 1
            if self.st == 21:
                self.st = 1
            
            if self.st == 10 and self.t % 2 == 0:
                self.image = Pterodactel.image1
                self.t += 1
            elif self.st == 10 and self.t % 2 != 0:
                self.image = Pterodactel.image2
                self.t += 1
                
                
            self.rect.x -= 10
            if self.rect.x == -100:
                self.rect.x = pos_p + random.randrange(300, 1200, 100)
                if pos_k <= self.rect.x + 400 and pos_k > 1200:
                    self.rect.x = 1200
                elif pos_k >= self.rect.x + 400 and pos_k > 1200:
                    self.rect.x += 300
                
            
            if args.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args.pos):
                self.kill()
                nn += 1


class GameOver(pygame.sprite.Sprite):
    image = load_image("game_over.png")
    image0 = load_image("game_over0.png")


    def __init__(self, group):
        super().__init__(group)
        self.image = GameOver.image0
        self.st = 0
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        

    def update(self, args):
        global HI_SCORE
        if running_sprite == False:
            self.image = GameOver.image
            if score > HI_SCORE:
                HI_SCORE = score
                r = open('hi_score_dino.txt', encoding="cp1251", mode="w")
                r.write(str(HI_SCORE))
                r.close()



Grass1(all_sprites)
Grass2(all_sprites)
Dino(dino_and_kaktus)
Kaktus1(dino_and_kaktus)
Cloud1(all_sprites)
Cloud2(all_sprites)
Pterodactel(dino_and_kaktus)
Pterodactel2(dino_and_kaktus)
GameOver(all_sprites)

pygame.display.set_caption("PythonDino")



x = 0
y = 0
fps = 60
running = True
clock = pygame.time.Clock()
 
while running:
    x = 0
    clock.tick(fps)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = 1
            if event.key == pygame.K_DOWN:
                y = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                    y = 0
    
    all_sprites.draw(screen)
    all_sprites.update(event)
    dino_and_kaktus.draw(screen)
    dino_and_kaktus.update(event)
    
    
    a = pygame.font.Font(None, 25)
    b = a.render(f'Your score: {score}', 1, WHITE)
    xt = 1020
    yt = 300
    screen.blit(b, (xt, yt))
    
    if running_sprite == False:
        o = pygame.font.Font(None, 25)
        i = o.render(f'hi_score: {HI_SCORE}', 1, WHITE)
        xu = 890
        yu = 300
        screen.blit(i, (xu, yu))
    
    if nn == 3: 
        v = pygame.font.Font(None, 100)
        j = v.render('HACKER DETECTED!!!', 1, RED)
        xi = 0
        yi = 0
        screen.blit(j, (xi, yi))
    
    pygame.display.flip()

pygame.quit()
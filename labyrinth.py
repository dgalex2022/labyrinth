from typing import Any
from pygame import *
init()
display.set_caption('Лабиринт')                     #название
window=display.set_mode((700,500))                  #экран
window.fill((255,255,255))

play = image.load('play1.png')              #загрузка изображений
kill = image.load('kill1.png')              #загрузка изображений
#step_sound=mixer.Sound('steps.ogg')         #загрузка музыки

class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        sprite.Sprite.__init__(self)
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):                                                           #класс игрока
    def __init__(self,picture,x_speed,y_speed,w,h,x,y):
        super(). __init__(picture,w,h,x,y)
        self.x_speed=x_speed
        self.y_speed=y_speed
    def update(self): 
        if packman.rect.x <= 700-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, walls, False)  #провкка касаниий(все касания со стенами)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)    #проверка на прохождение через стену
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if packman.rect.y <= 500-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed

        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
              
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)  



        if packman.rect.x <= 700-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched_breaking = sprite.spritecollide(self, breaking_walls, False)  #провкка касаниий(все касания со стенами)
        if self.x_speed > 0: 
            for p in platforms_touched_breaking:
                self.rect.right = min(self.rect.right, p.rect.left)    #проверка на прохождение через стену
        elif self.x_speed < 0: 
            for p in platforms_touched_breaking:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if packman.rect.y <= 500-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed

        platforms_touched_1 = sprite.spritecollide(self, breaking_walls, False)
        if self.y_speed > 0: 
            for p in platforms_touched_breaking:
              
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0: 
            for p in platforms_touched_breaking:
                self.rect.top = max(self.rect.top, p.rect.bottom)


        #step_sound.play(0,100,0)
    def fire(self):
        bullet = Bullet('bullet.jpg', self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)


class Enemy(GameSprite):                          #класс врага
    side = "down"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image ,size_x, size_y , player_x, player_y )
        self.speed = player_speed

    def update(self):                            #движение врага
        if self.rect.y <= 270:
            self.side = "up"
        if self.rect.y >= 500-60:
            self.side = "down"
        if self.side == "down":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed



class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image ,size_x, size_y , player_x, player_y)
        self.speed = player_speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700+10:  #при касании исчезнуть
            self.kill()





walls = sprite.Group() 
bullets = sprite.Group()  
enemies =  sprite.Group()                                         #создание группы
money = sprite.Group()
breaking_walls = sprite.Group()

wall1=GameSprite('wall4.jpeg',20,400,100,250)                           #создание стен
wall2=GameSprite('wall4.jpeg',200,20,100,250)
wall3=GameSprite('wall4.jpeg',500,20,375,250)
wall4=GameSprite('wall4.jpeg',500,20,100,150)
wall5=GameSprite('wall4.jpeg',20,100,500,0)
wall6=GameSprite('wall4.jpeg',20,100,350,50)
wall7=GameSprite('wall4.jpeg',20,100,200,0)
wall8=GameSprite('wall4.jpeg',20,100,500,150)

breaking_wall_1=GameSprite('breaking_wall.jpg',20,100,100,150)  
breaking_wall_2=GameSprite('breaking_wall.jpg',20,50,200,100)
breaking_wall_3=GameSprite('breaking_wall.jpg',20,400,500,270)

money1=GameSprite('money.png',50,50,125,280)               
money2=GameSprite('money.png',50,50,225,0)
money3=GameSprite('money.png',50,50,525,0)
money4=GameSprite('money.png',50,50,550,180)
finish_1=GameSprite('money.png',50,50,600,400)

packman=Player('play1.png',0,0,50,50,5,400)                            #создание игрока
enemy1=Enemy('kill1.png',225,400,60,60,5)
enemy2=Enemy('kill1.png',375,400,60,60,7)

walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8)                           #добавление объектов в группу
enemies.add(enemy1,enemy2)
money.add(money1,money2,money3,money4,finish_1)
breaking_walls.add(breaking_wall_1,breaking_wall_2,breaking_wall_3)



run=True
finish_A=False
finish_B=False
finish_C=False
finish_D=False
finish_E=False
finish=False
lose=False
while run:
    time.delay(50)
    window.fill((255,255,255))
    if finish !=True and lose != True:
        if sprite.collide_rect(packman, finish_1):   #финиш              
            finish_A = True
            finish_1.kill()
        if sprite.collide_rect(packman, money1): 
            money1.kill()            
            finish_B = True
        if sprite.collide_rect(packman, money2):                
            finish_C = True
            money2.kill()  
        if sprite.collide_rect(packman, money3):                
            finish_D = True
            money3.kill()  
        if sprite.collide_rect(packman, money4):                
            finish_E = True
            money4.kill()  
        if finish_A and finish_B and finish_C and finish_D and finish_E:
            finish=True
        if sprite.spritecollideany(packman,enemies):
            lose = True
        
    
        sprite.groupcollide(enemies, bullets, True, True)            #уничтожение обьектов
        sprite.groupcollide(walls, bullets, False, True)
        sprite.groupcollide(breaking_walls, bullets, True, True)
        #sprite.groupcollide(packman, money, False, True)
        walls.draw(window)        #отрисовка
        bullets.draw(window)
        enemies.draw(window)
        money.draw(window)
        breaking_walls.draw(window)
        '''money1.reset()
        money2.reset()
        money3.reset()
        money4.reset()'''
        packman.reset()
        #finish_1.reset()

        packman.update()
        bullets.update()
        enemies.update()
        money.update()
        breaking_walls.update()
    
        
                                                    
    
    for e in event.get():                        #назначение клавиш 
        if e.type==QUIT:
            run=False
        elif e.type==KEYDOWN:
            if e.key==K_a:
                packman.x_speed=-5
            elif e.key==K_d:
                packman.x_speed=5
            elif e.key==K_w:
                packman.y_speed=-5
            elif e.key==K_s:
                packman.y_speed=5
            elif e.key==K_e:
                packman.fire()

        elif e.type==KEYUP:
            if e.key==K_a:
                packman.x_speed=0
            if e.key==K_d:
                packman.x_speed=0
            if e.key==K_w:
                packman.y_speed=0
            if e.key==K_s:
                packman.y_speed=0
                
            

        '''elif e.type== MOUSEBUTTONDOWN:
            packman.shot()                     #новый модуль shot (кнопка мыши пкм)
        elif e.type== K_e:
            packman.interact()                 #новый модуль interact'''
        
    display.update()

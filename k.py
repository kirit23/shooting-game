import pgzrun
import random

WIDTH=1200
HEIGHT=600

#defining colors

WHITE= (255,255,255)
BLUE= (0,0,255)

#creating charaters
ship = Actor("spaceship")
enemy = Actor("enemy")

ship.pos=(WIDTH//2, HEIGHT - 60)

speed=5

#creating list for bullets 
bullets=[]
#list for enemies
enemies=[]

#creating matrix of enemies - > 8 cols and 4 rows
for x in range (8): #cols
    for y in range(4):
        enemies.append(Actor("enemy"))
        #enemies in starlight line 
        enemies[-1].x= 100 + 50*x
        #slowly enemies have to come down from top 
        enemies[-1].y = 80 +50*y


        score=0
        direction=1
        ship.dead=False
        ship.countdown=50

#for updating the score 
def displayscore():
    screen.draw.text(str(score),(50,30))

def gameOver():
    screen.draw.text("GAME OVER",(250,300))


def on_key_down(key):
    if ship.dead==False:
        if key==keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y = 50


def update():
    global direction, score
    moveDown = False 

    #ship movement with arrow keys 
    if ship.dead==False:
        
        if keyboard.left:
            ship.x -= speed 
            if ship.x >= WIDTH:
                ship.x =WIDTH

#if bullet reaches top of screen we remove that bullet from the lost 
#else list would be too long
    for bullet in bullets:
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

#check postion of last enemy 
    if len(enemies) == 0:
       gameOver()

    if len(enemies) >0 and enemies[-1].x > WIDTH-80 or enemies[-1].x < 80:
       moveDown=True
       direction = direction * -1

    for enemy in enemies:
        enemy.x += 5 * direction 
        if moveDown==True:
         enemy.y += 100 
        if enemy.y > HEIGHT:
         enemies.remove(enemy)
        

#checking the collision of bullet and enemy while movind down 
#iterate through the bullets list and check for collision 
        for bullet in bullets:
            if enemy.colliderect(bullet):
             score += 100
            #we will destroy both  enemies and bullets
             bullets.remove(bullet)
             enemies.remove(enemy)
             if len (enemies) ==0:
                gameOver()
    #checking if enemy hits ship 
        if enemy.colliderect(ship):
         ship.dead=True

    if ship.dead:
     ship.countdown -=1
    if ship.countdown==0:
     ship.dead=False
     ship.coundown = 90

def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()

#ship to be draw last 
    if ship.dead==False:
     ship.draw()
    displayscore()
    if len(enemies) ==0:
        gameOver()


pgzrun.go()
       

        





























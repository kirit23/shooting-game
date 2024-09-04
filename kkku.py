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
        enemies.append(actor("enemies"))


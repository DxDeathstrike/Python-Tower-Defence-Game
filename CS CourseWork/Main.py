#####################library files########################
import pygame
import time
import random
import Levels as L

################this inistialises the pygame settings##########################
pygame.init()

#set up screen dimensions
display_width = 1080
display_height = 600

#setup the defaul time 
start_time = 0



size = display_width,display_height = 1080,600
#colour constants for button backgrounds and screen backgrounds
BLACK = (0,0,0)
WHITE = (255,255,255)

RED = (200,0,0)
GREEN = (0,200,0)
YELLOW = (255,255,0)

BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)
LIGHT_YELLOW = (255,255,51)

AQUA = (0, 128, 128)
GRAY = (190, 190, 190)





#creates the screen area - will need one for each screen when using background images to be done next
# gamedisplay is the screen area where we draw things to from now on

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()    ### this enables us to set frame rate


##images


Menu = pygame.image.load("CS Images/Main Menu/new Menu.png").convert_alpha()      #Menu image
Menu = pygame.transform.scale(Menu, size) # scale images to fit the games size


Map = pygame.image.load("CS Images\Map\Map.png").convert_alpha() 
Map = pygame.transform.scale(Map, size)


play_button = pygame.image.load("CS Images/Main Menu/Buttons/play button.png").convert_alpha()
play_button_big = pygame.transform.scale_by(play_button, 2.4)

scoreboard_button = pygame.image.load("CS Images/Main Menu/Buttons/scoreboard button.png").convert_alpha()
scoreboard_button_big = pygame.transform.scale_by(scoreboard_button, 2.4)


quit_button = pygame.image.load("CS Images/Main Menu/Buttons/quit button.png").convert_alpha()
quit_button_big = pygame.transform.scale_by(quit_button, 2.4)


test_font = pygame.font.Font("Font\Pixeltype.ttf",50)  # imports the font i want to use


platform_button = pygame.image.load("CS Images\Towers\Platform\platform.png").convert_alpha()




#this creates our buttons parameters img,x,y, function to run.
def button(img,x,y,action):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Create a rectangle from the image and set it to the correct position:

    button_rect = img.get_rect(center = (x,y))

    # Check if a point (mouse_poss) is inside a rectangle (button_rect):

    if button_rect.collidepoint(mouse_pos):
        
        if click[0] == 1 and action != None:
            action()         

    gameDisplay.blit(img, button_rect)







def create(x,y):
    archer_tower = Tower((x),(y),0.24,"t1","Archer")
    archer_tower_g.add(archer_tower)
        













def display_score(start_time,time):
    score = 0
    if time >=30:
        score = int((pygame.time.get_ticks() - start_time) / 245) 
        score_surf = test_font.render(f'Score: {score}',False, WHITE)
        score_rect = score_surf.get_rect(center = (100,80))
        gameDisplay.blit(score_surf,score_rect)
    return(score)


#this displays the time since game has been running
def display_time(start_time):
    time = int(((pygame.time.get_ticks() - start_time) / 1000)) 
    timer_surf = test_font.render(f'Time: {time}',False, WHITE)
    timer_rect = timer_surf.get_rect(center = (100,50))
    gameDisplay.blit(timer_surf,timer_rect)
    return(time)






def temp():
    print("worked")


#creating the sprite class for Entities
class Entity(pygame.sprite.Sprite):
    def __init__ (self,pos_x,pos_y,speed,tier,group):
        super().__init__()
        self.sprites = []
        self.sprites_died = []
        self.animate = True
        self.tier = str(tier)
        self.die = False
        self.speed = speed
        self.group_t1 = group



        self.CHECKPOINT_1 = (
    (999, 582),(988, 493),(969, 472),(944, 462),
    (873, 454),(846, 438),(821, 413),(806, 367),
    (815, 314),(837, 280),(897, 263),(972, 244),
    (993, 215),(1008, 172),(1008, 172),(997, 127),
    (975, 93),(938, 74),(869, 68),(800, 66),(743, 43),
    (698, 43),(659, 66),(512, 68),(421, 74),(392, 105),
    (374, 146),(372, 211),(341, 248),(251, 269),(204, 291)
    ,(188, 330),(180, 410),(143, 440),(120, 454),(-25, 452)
)


        
        self.CHECKPOINT_1 = list(self.CHECKPOINT_1)




        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/1.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/2.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/3.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/4.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/5.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/6.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/7.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/8.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/9.png").convert_alpha(), 0.4)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/walk/10.png").convert_alpha(), 0.4)))


        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/1.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/2.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/3.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/4.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/5.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/6.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/7.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/8.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/9.png").convert_alpha(), 0.4)))
        self.sprites_died.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Entities/{self.tier}/Die/10.png").convert_alpha(), 0.4)))




        self.current_sprite = 0
        self.current_sprite_died = 0

        self.image = self.sprites[self.current_sprite]
        self.image_died = self.sprites_died[self.current_sprite_died]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

    def gets_hit(self):
        return()




    def died(self):
        self.die = True

        self.animate_off()
        
        if self.die == True:
            self.current_sprite_died += self.speed

            if self.current_sprite_died >= len(self.sprites_died):
                self.kill()
            try:
                self.image = self.sprites_died[int(self.current_sprite_died)]
            except Exception:
                pass






    def animate_on(self):
        self.animate = True

    def animate_off(self):
        self.animate = False


    def update(self):
        if self.animate == True:
            L.Map(self.CHECKPOINT_1,self.group_t1,self.rect)
            self.current_sprite += self.speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]

        # keys = pygame.key.get_pressed()

        # if keys[pygame.K_UP]:
        #     self.died()
#creating the sprite class for objects
class Tower(pygame.sprite.Sprite):
    def __init__ (self,pos_x,pos_y,speed,tier,type):
        super().__init__()
        self.sprites = []
        self.animate = False
        self.tier = "1"
        self.tier = self.tier = tier
        self.type = str(type)
        self.destroyed = False
        self.speed = speed

        self.static = (pygame.transform.scale_by(pygame.image.load(f"CS Images/Towers/{self.type}/{self.tier}/1.png").convert_alpha(), 0.6))
        
        #self.static = (pygame.transform.scale_by(pygame.image.load(f"CS Images\Towers\{self.type}\{self.tier}\Static.png").convert_alpha(), 0.4))


        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Towers/{self.type}/{self.tier}/Shoot/1.png").convert_alpha(), 0.6)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Towers/{self.type}/{self.tier}/Shoot/2.png").convert_alpha(), 0.6)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Towers/{self.type}/{self.tier}/Shoot/3.png").convert_alpha(), 0.6)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Towers/{self.type}/{self.tier}/Shoot/4.png").convert_alpha(), 0.6)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Towers/{self.type}/{self.tier}/Shoot/5.png").convert_alpha(), 0.6)))
        self.sprites.append((pygame.transform.scale_by(pygame.image.load(f"CS Images/Towers/{self.type}/{self.tier}/Shoot/6.png").convert_alpha(), 0.6)))





        self.current_sprite = 0
        self.current_sprite_arrow = 0


        #self.image = self.static
        self.image = self.sprites[self.current_sprite]
  

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

    def arrow(self):
        self.animate = True
        
        if self.animate == True:
            self.current_sprite_arrow += self.speed
            

            if self.current_sprite_died >= len(self.sprites_died):
                self.kill()
            try:
                self.image = self.sprites_died[int(self.current_sprite_died)]
            except Exception:
                pass




    def animate_on(self):
        self.animate = True

    def animate_off(self):
        self.animate = False



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.die = True

        if self.animate == True:
            self.current_sprite += self.speed

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            self.image = self.sprites[int(self.current_sprite)]
        elif self.animate == False:
            self.image = self.static



#class Platform(pygame.sprite.Sprite):

























#making each wave group here

total_entities = pygame.sprite.Group()
wave2_t2 = pygame.sprite.Group()


wave1_t1 = pygame.sprite.Group()
for i in range(5):
    w = i * 250                                         # makes distance between each entity so its not clustered
    t1 = Entity((1003),(625 + w),0.34,"t1",wave1_t1)    # makes the entity
    wave1_t1.add(t1)                                    # adds the entity to the group
    total_entities.add(t1)                              # adds the entity to the otal entity group




archer_tower_g = pygame.sprite.Group()
archer_tower = Tower((890),(505),0.24,"t1","Archer")
archer_tower_g.add(archer_tower)





#this is for text boxes on the screens i.e. titles etc
def text_objects(text, font):
    textSurface = test_font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

# main menu screen
def main_menu():

    intro = True      #### will display until we set to false
    
    while intro:
        for event in pygame.event.get():
            #checks that we havent hit the x in the window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #set our screen background colour      
        
        gameDisplay.fill(GRAY)
        # display an image in the background
        
        gameDisplay.blit(Menu, (0,0))
        #loads the image

        #sets the text size and font for title -could be declared globally
        largeText = pygame.font.SysFont("tahoma",50)
        TextSurf, TextRect = text_objects("MAIN MENU", largeText)
         #sets the position of title text - i just changed the display_height divided by for vertical position
        TextRect.center = ((display_width/2),(170))
        gameDisplay.blit(TextSurf, TextRect)

        #call button function to create the buttons
        #these buttons trigger different game states
  
        button(play_button_big,(display_width//2),270,game_loop)
        button(scoreboard_button_big,(display_width//2),360,score_board)
        button(quit_button_big,(display_width//2),450,quitgame)

        pygame.display.update()
        clock.tick(30)  ### set frame rate to 30
#main game loop - change your main game play loop to a procedure so that it runs from the button.




def game_loop():
    intro = False      
    play = True
    scoreboard = False
    T_Entity = len(total_entities)
    start_time = pygame.time.get_ticks() 
    while play:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



##temp input, change to detect arrow collision
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                t1.die = True
            if keys[pygame.K_RIGHT]:
                archer_tower.animate = True
            
            if keys[pygame.K_LEFT]:
                archer_tower.animate = False

        if len(total_entities) == 0:
            start_time = 0


        gameDisplay.fill(GRAY)
        gameDisplay.blit(Map, (0,0))
        current_time = display_time(start_time)
        current_score = display_score(start_time,current_time)

        if current_time > 5:
            wave1_t1.draw(gameDisplay)
            wave1_t1.update()
            if t1.die == True:
                t1.died()

                    

        if T_Entity == 0:
            
            w = i * 200                                      
            new_entity=Entity((1003),(625 + w),0.34,"t2",wave2_t2)
            wave2_t2.add(new_entity)
            total_entities.add(new_entity)

        wave2_t2.draw(gameDisplay)
        wave2_t2.update()

        # # check for collision between player and enemy
        # hits= pygame.sprite.spritecollide(player,mob_group,True)
        # # if hits:
        # #     score_board()
        # for hit in hits:
        #     newenemy=Mob2()
        #     mob_group.add(newenemy)
        #     all_sprites_group.add(newenemy)

        # moving_t1.draw(gameDisplay)
        # moving_t1.update()
        # if time > 5:
        #     if t1.die == True:
        #         t1.died()
        #     if t1.die == False:
        #         L.Map(L.CHECKPOINT_1,moving_t1,t1.rect,1)
        


        #button(platform_button,75,375,create(75,375))
        button(platform_button,300,355,temp)
        button(platform_button,495,160,temp)
        button(platform_button,885,170,temp)
        button(platform_button,695,325,temp)
        button(platform_button,925,360,temp)
        button(platform_button,890,540,temp)




        archer_tower_g.draw(gameDisplay)
        archer_tower_g.update()


        # time.sleep(6)
        # pos = pygame.mouse.get_pos()
        # print(pos)




        


        #button(play_button_big,150,450,game_loop)
        #button(scoreboard_button_big,350,450,score_board)
        #button(quit_button_big,550,450,quitgame)



        pygame.display.update()
        clock.tick(30)


#scoreboard -same set up as game_loop whilst we text menu and structure. will be added later
def score_board():
    #we may use these variables for a back button.
    intro = False
    play = False
    scoreboard = True

    while scoreboard:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(AQUA)
        largeText = pygame.font.SysFont("TAHOMA",50)
        TextSurf, TextRect = text_objects("Scoreboard Here", largeText)
        TextRect.center = ((display_width/2),(display_height/5))
        gameDisplay.blit(TextSurf, TextRect)



        button(play_button_big,150,450,game_loop)
        button(scoreboard_button_big,550,450,score_board)
        button(quit_button_big,925,450,quitgame)


        pygame.display.update()
        clock.tick(30)

    

#this stops the game from running   
def quitgame():
    pygame.quit()
    quit()

if __name__ == "__main__":
    main_menu()




















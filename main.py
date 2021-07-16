import pygame 

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)


class Ball():

    def __init__(self, X,Y, radius, screen):
        self.x = X
        self.y = Y
        self.radius = radius
        self.screen = screen
        self.vert_speed = 0
        self.horz_speed = -10
        self.rect = pygame.draw.circle(self.screen, WHITE, (self.x,self.y), self.radius)

        self.left =  self.x - self.radius
        self.right = self.x + self.radius
        self.top = self.y - self.radius
        self.bottom = self.y + self.radius

    def draw(self):
        self.rect = pygame.draw.circle(self.screen, WHITE, (self.x,self.y), self.radius)

    def move(self):
        self.x += self.horz_speed
        self.y += self.vert_speed

    def flip_horz_speed(self):
        self.horz_speed = -self.horz_speed

    def flip_vert_speed(self):
        self.vert_speed = -self.vert_speed

class paddel():
    
    def __init__(self, X,Y,screen):
        self.x = X
        self.y = Y
        self.width = 50
        self.height = 100
        self.screen = screen
        self.vert_speed = 10
        self.rect =  pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.width, self.height))
        

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.width, self.height))

    def move_up(self):
        
        if self.y > 0:
            self.y -= self.vert_speed


    def move_down(self):
        
        if self.y < self.screen.get_height() - self.height:
            self.y += self.vert_speed


def collision(ball, paddel):

    ball_tlc_x = ball.x - ball.radius
    ball_tlc_y = ball.y - ball.radius


    if paddel.x <= ball_tlc_x and ball_tlc_x <= paddel.x + paddel.width and paddel.y <= ball_tlc_y and ball_tlc_y <= paddel.y+paddel.height:
        print("collison")
    

    
# def in_paddel(ball, paddel):

#     ball_top_y = ball.y - ball.radius
#     ball_top_x = ball.x - ball.radius

#     paddel_bottom_x =  paddel.x + paddel.width
#     paddel_bottom_y =  paddel.y + paddel.height

#     if ball_top_y >= paddel.y and ball_top_y <= paddel_bottom_y and ball_top_x >= paddel.x and ball_top_x <= paddel_bottom_y:
#         print("yep") 



def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Pong!")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    screen.blit(background, (0,0))
    pygame.display.flip()

    clock = pygame.time.Clock()

    ball = Ball(305,305, 10, screen)

    player_left = paddel(0, 200, screen)
    player_right =  paddel(WIDTH-50, 200, screen)



    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            player_right.move_up()
        if keys[pygame.K_DOWN]:
            player_right.move_down()

        if keys[pygame.K_w]:
            player_left.move_up()

        if keys[pygame.K_s]:
            player_left.move_down()


        ball.move()

        collision(ball, player_left)   

        collision(ball, player_right)

        #check top
        if ball.y - ball.radius <= 0:
            ball.flip_vert_speed()
        #check bottom
        if ball.y + ball.radius >= HEIGHT:
            ball.flip_vert_speed()

        #check left
        if ball.x - ball.radius <= 0:
            ball.flip_horz_speed()

        #check right
        if ball.x + ball.radius >= WIDTH:
            ball.flip_horz_speed()

        #check left paddel collison
        
    
        #check right paddel collision
        


        screen.blit(background, (0,0))

        ball.draw()
        player_left.draw()
        player_right.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()
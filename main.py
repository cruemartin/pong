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
        self.vert_speed = 4
        self.horz_speed = 4
        self.rect = None

    def draw(self):
        self.rect = pygame.draw.circle(self.screen, WHITE, (self.x,self.y), self.radius)

    def move(self):
        self.x += self.horz_speed
        self.y += self.vert_speed

    def flip_horz_speed(self):
        self.horz_speed = -self.horz_speed

    def flip_vert_speed(self):
        self.vert_speed = -self.vert_speed

class Pattel():
    
    def __init__(self, X,Y,screen):
        self.x = X
        self.y = Y
        self.screen = screen
        self.vert_speed = 4
        self.rect =  None
        self.width = 50
        self.height = 100

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.width, self.height))

    def move_up(self):
        
        if self.y > 0:
            self.y -= self.vert_speed


    def move_down(self):
        
        if self.y < self.screen.get_height() - self.height:
            self.y += self.vert_speed




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

    ball = Ball(300,300, 10, screen)

    player_left = Pattel(0, 200, screen)


    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            player_left.move_up()
        if keys[pygame.K_DOWN]:
            player_left.move_down()




        ball.move()

        #check top
        if ball.y <= 0:
            ball.flip_vert_speed()
        #check bottom
        if ball.y >= HEIGHT:
            ball.flip_vert_speed()

        #check left
        if ball.x <= 0:
            ball.flip_horz_speed()

        #check right
        if ball.x >= WIDTH:
            ball.flip_horz_speed()

        screen.blit(background, (0,0))

        ball.draw()
        player_left.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()
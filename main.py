import pygame 

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

WIN_SCORE = 3


class Ball():
    """This a class for the ball object"""

    def __init__(self, X,Y, radius, screen):
        self.x = X
        self.y = Y
        self.radius = radius
        self.screen = screen
        self.vert_speed = 5
        self.horz_speed = -5
        self.rect = pygame.draw.circle(self.screen, GREEN, (self.x,self.y), self.radius)

        self.left =  self.x - self.radius
        self.right = self.x + self.radius
        self.top = self.y - self.radius
        self.bottom = self.y + self.radius

    def draw(self):
        self.rect = pygame.draw.circle(self.screen, GREEN, (self.x,self.y), self.radius)

    def move(self):
        self.x += self.horz_speed
        self.y += self.vert_speed

    def flip_horz_speed(self):
        self.horz_speed = -self.horz_speed

    def flip_vert_speed(self):
        self.vert_speed = -self.vert_speed

    def collision(self, paddel):

        ball_tlc_x = self.x - self.radius
        ball_tlc_y = self.y - self.radius

        return paddel.x <= ball_tlc_x and ball_tlc_x <= paddel.x + paddel.width and paddel.y <= ball_tlc_y and ball_tlc_y <= paddel.y+paddel.height
           

class Paddel():
    
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


def court(screen):
    
    pygame.draw.line(screen, WHITE, (screen.get_width()/2 -3 ,0), (screen.get_width()/2 - 3 , screen.get_height()) , width= 3 )


def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Pong!")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    screen.blit(background, (0,0))
    pygame.display.flip()

    clock = pygame.time.Clock()

    ball = Ball(305,305, 10, screen)

    player_left = Paddel(0, 200, screen)
    player_right =  Paddel(WIDTH-50, 200, screen)

    player_left_score = 0
    player_right_score = 0

    player_left_win = False
    player_right_win = False



    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

                if event.key == pygame.K_p:
                    pause(screen)

                if player_right_win or player_left_win and event.key == pygame.K_r:
                    main()


        #check for win
        if player_left_score == WIN_SCORE:
            player_left_win = True
        if player_right_score == WIN_SCORE:
            player_right_win = True
        
        #if there is a win display the win message
        if player_right_win or player_left_win:
            win_font = pygame.font.Font(None, 75)
            message = ""
            if player_left_win:
                message = "Left Wins!"
            if player_right_win:
                message = "Right Wins!"

            win_text = win_font.render(message, 1, WHITE)

            screen.blit(win_text, (screen.get_width()/2 - win_text.get_width()/2, screen.get_height()/2 - win_text.get_height()/2))

        #check keys pressed for paddel movement
        keys = pygame.key.get_pressed()

        #right paddel
        if keys[pygame.K_UP]:
            player_right.move_up()
        if keys[pygame.K_DOWN]:
            player_right.move_down()
        #left paddel
        if keys[pygame.K_w]:
            player_left.move_up()
        if keys[pygame.K_s]:
            player_left.move_down()


        ball.move()

        #check top
        if ball.y - ball.radius <= 0:
            ball.flip_vert_speed()
        #check bottom
        if ball.y + ball.radius >= HEIGHT:
            ball.flip_vert_speed()

        #check left
        if ball.x - ball.radius <= 0:
            player_right_score += 1
            ball.flip_horz_speed()

        #check right
        if ball.x + ball.radius >= WIDTH:
            player_left_score += 1
            ball.flip_horz_speed()

        #check left paddel collison
        if ball.collision(player_left):
            ball.x = player_left.x + player_left.width + ball.radius
            ball.flip_horz_speed()

        #check right paddel collision
        if ball.collision(player_right)  :
            ball.x = player_right.x - ball.radius
            ball.flip_horz_speed()


        screen.blit(background, (0,0))

        #check for win
        if player_left_score == 10:
            player_left_win = True
        if player_right_score == 10:
            player_right_win = True
        
        #if there is a win display the win message
        if player_right_win or player_left_win:
            win_font = pygame.font.Font(None, 75)
            message = ""
            if player_left_win:
                message = "Left Wins!"
            if player_right_win:
                message = "Right Wins!"

            win_text = win_font.render(message, 1, WHITE)

            screen.blit(win_text, (screen.get_width()/2 - win_text.get_width()/2, screen.get_height()/2 - win_text.get_height()/2))

            reset_font = pygame.font.Font(None,50)
            reset_text = reset_font.render("Press [r] to play again or [Esc] to quit!", 1, WHITE)
            screen.blit(reset_text, (screen.get_width()/2 - reset_text.get_width()/2, screen.get_height()/2 + (reset_text.get_height()/2 + win_text.get_height())))
        
        else:

            #display scrore
            font = pygame.font.Font(None, 50)
            text = font.render(str(player_left_score), 1, WHITE)
            screen.blit(text, (screen.get_width()/2 - (text.get_width() + 10) , screen.get_height()/2 - 25))
            text = font.render(str(player_right_score), 1, WHITE)
            screen.blit(text, (screen.get_width()/2 + 5, screen.get_height()/2 - 25))


            #draw
            court(screen)
            ball.draw()
            player_left.draw()
            player_right.draw()

        pygame.display.flip()

def title_screen():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Pong!")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    screen.blit(background, (0,0))
    pygame.display.flip()

    clock = pygame.time.Clock()


    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                main() 

        title_font = pygame.font.Font(None, 100)
        title = title_font.render("PONG!", 1, WHITE)
        screen.blit(title, ((screen.get_width()/2) - title.get_width()/2, screen.get_height()/3))
        instruction_font = pygame.font.Font(None, 50)
        instruction = instruction_font.render("Press [2] to start a 2 player game!", 1, WHITE)
        screen.blit(instruction, (screen.get_width()/2 - instruction.get_width()/2, screen.get_height()/2))
        signature_font = pygame.font.Font(None, 25)
        signature = signature_font.render("Made by Crue Martin using pygame!", 1, WHITE)
        screen.blit(signature, (screen.get_width()/2 - signature.get_width()/2, screen.get_height() - (signature.get_height() + 10)))

        pygame.display.flip()

def pause(screen):

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                return
        

        screen.fill(BLACK)

        paused_font = pygame.font.Font(None, 80)
        paused = paused_font.render("Game Paused", 1, WHITE)
        screen.blit(paused, (screen.get_width()/2 - paused.get_width()/2, screen.get_height()/3))
        instruction_font = pygame.font.Font(None, 50)
        instruction = instruction_font.render("Press [c] to continue...",1, WHITE)
        screen.blit(instruction, (screen.get_width()/2 - instruction.get_width()/2, screen.get_height()/2))

        pygame.display.flip()

if __name__ == "__main__":
    title_screen()
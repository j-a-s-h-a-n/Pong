import pygame



pygame.init()


class Setup():
   width = 900
   height =600
   black = (0, 0, 0)
   PINK = (204, 0, 204)
   GREEN = (51, 255, 51)
   GREEEN = (0, 102, 0)
   border = pygame.Rect(width / 2 -5, 0, 10, height)
   pong = pygame.Rect(10, height/2-50, 15, 100)
   pong2 = pygame.Rect(875, height/2-50,15, 100)
   ball = pygame.Rect(width/2,height/2, 15, 15)
   win = pygame.display.set_mode((width,height))
   pygame.display.set_caption("Pong")
   vel = 10
   ball_x=5
   ball_y=5
   font = pygame.font.Font('comicz.ttf', 30)
   def drawWindow(self,leftscore,rightscore):
       self.win.fill(self.black)
       pygame.draw.rect(self.win,self.GREEEN,self.border)
       pygame.draw.rect(self.win, self.GREEN, self.pong)
       pygame.draw.rect(self.win, self.GREEN, self.pong2)
       pygame.draw.rect(self.win,self.PINK,self.ball)
       left_score = self.font.render(f"{leftscore}", 1, window.GREEEN)
       right_score = self.font.render(f"{rightscore}", 1, window.GREEEN)
       self.win.blit(left_score, (23, 10))
       self.win.blit(right_score, (855, 10))
       pygame.display.update()

   def left_move(self,keys_pressed, left):
       if keys_pressed[pygame.K_s] and left.y<self.height-left.height:
           left.y+=self.vel
       if keys_pressed[pygame.K_w] and left.y>0:
           left.y -= self.vel

   def right_move(self, keys_pressed, right):
       if keys_pressed[pygame.K_DOWN] and right.y < self.height - right.height:
           right.y += self.vel
       if keys_pressed[pygame.K_UP] and right.y > 0:
           right.y -= self.vel
   def ball_move(self, ball,y1,y2):
       ball.x-=self.ball_x
       ball.y-=self.ball_y
       if ball.y>595-5:
           self.ball_y*=-1
       if ball.y<5:
           self.ball_y *=-1
       if ball.x == self.pong2.x and ball.y == self.pong2.y:
           self.ball_x *=-1
           self.ball_y *= -1
       if (ball.x > 875-15 and ball.x < 870) and ball.y in y2:
           self.ball_x *= -1
       if (ball.x < 10+15 and ball.x > 15) and ball.y in y1:
           self.ball_x *= -1
   def reset(self):
       self.ball.x=self.width/2
       self.ball.y=self.height/2
window = Setup()
run=True

def main():
    run = True
    clock = pygame.time.Clock()
    FPS=60
    leftscore = 0
    rightscore = 0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        window.left_move(keys_pressed, window.pong)
        window.right_move(keys_pressed, window.pong2)
        pongy = [x for x in range(window.pong.y, window.pong.y + window.pong.height)]
        pong2y = [x for x in range(window.pong2.y, window.pong2.y + window.pong.height)]
        window.ball_move(window.ball,pongy,pong2y)
        if window.ball.x > 900 or window.ball.x < 0:
            if window.ball.x > 900:
                leftscore += 1
            if window.ball.x < 0:
                rightscore += 1
            window.reset()

main()
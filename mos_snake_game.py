from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=400,bg="#99CCCC")
canvas.pack()
class Snake:
    def __init__(self):
        self.canvas=canvas
        self.side_of_snake = 20
        self.position_of_snake=[[200,200],[210,200],[220,200]]
        self.direction_of_snake="left"
        self.final_position_of_snake=[260,200]
        self.position_of_food=[0,0]
        self.frame_width = 500
        self.frame_height = 400
        self.x1x2y1y2_of_foof=[]
        self.score=0
        self.canvas.bind ('<Key>',self.kb_calllback)
        self.canvas.focus_set()
#keybroad
    def kb_calllback(self,event):
        print(event.char)
        d=self.direction_of_snake
        if event.char=='w' or event.char=='W' :
            if d=="down":
                self.direction_of_snake="down"
            else:
                self.direction_of_snake="up"
        elif event.char=='s' or event.char=='S' :
            if d=="up":
                self.direction_of_snake="up"
            else:
                self.direction_of_snake="down"
        elif event.char=='a' or event.char=='A' :
            if d=="right":
                self.direction_of_snake="right"
            else:
                self.direction_of_snake="left"
        elif event.char=='d' or event.char=='D' :
            if d=="left":
                self.direction_of_snake="left"
            else:
                self.direction_of_snake="right"
#create display
    def create_display(self):
        self.canvas.delete("all")
        draw_border_area_of_snake_run = canvas.create_rectangle(45,65,455,375, fill="#003333")
        draw_area_of_snake_run = canvas.create_rectangle(50,70,450,370, fill="#99CCCC")  
        draw_show_score=canvas.create_text(250, 30,font=("Purisa", 16),text=("Your score : %d"%self.score),fill="#FFFFFF")
        self.draw_food()
        self.draw_snake()
#move snake
    def move_snake(self):
        self.create_display()
        ds=self.direction_of_snake
        ps=self.position_of_snake
        fps=self.final_position_of_snake
        n=len(ps)-1
        fps[0]=ps[n][0]
        fps[1]=ps[n][1]
        while n>0:
            ps[n][0] = ps[n-1][0]
            ps[n][1] = ps[n-1][1]
            n-=1
        if ds=="up":
            ps[0][1]-=20
        elif ds=="down":
            ps[0][1]+=20           
        elif ds=="left":
            ps[0][0]-=20
        elif ds=="right":
            ps[0][0]+=20
    def draw_snake(self):
        ps=self.position_of_snake
        side=self.side_of_snake
        for n in range (len(ps)):
            x=int(ps[n][0])
            y=int(ps[n][1])
            x1 = x-side/2
            y1 = y-side/2
            x2 = x+side/2
            y2 = y+side/2
            body_snake = canvas.create_rectangle(x1,y1,x2,y2,outline="#dbf", fill="#003333")
        self.cheak_snake_crash_wall()
        self.cheak_snake_eat_body()
        self.cheak_snake_eat_food()
    def draw_food(self):
        f=self.x1x2y1y2_of_foof
        draw_food = canvas.create_oval(f[0],f[1],f[2],f[3], fill="red")
    def random_food_snake(self):
        side=self.side_of_snake
        while True:
            random_x = random.randint (60,450)
            random_y = random.randint (80,370)
            x=int(random_x/side)*side
            y=int(random_y/side)*side
            x1 = int(x-side/2)
            y1 = int(y-side/2)
            x2 = int(x+side/2)
            y2 = int(y+side/2)
            self.position_of_food=[x,y]
            if [x,y] in self.position_of_snake:
                continue
            else:
                print(x1,y1,x2,y2)
                self.x1x2y1y2_of_foof=[x1,y1,x2,y2]
                break
    def cheak_snake_eat_food(self):
        if self.position_of_food == self.position_of_snake[0]:
            x=int(self.final_position_of_snake[0])
            y=int(self.final_position_of_snake[1])
            self.position_of_snake.append([x,y])
            self.random_food_snake()
            self.score+=1
    def cheak_snake_crash_wall(self):
        ps = self.position_of_snake
        side=self.side_of_snake
        if ps[0][0]<50+side/2 or ps[0][0]>450-side/2 or ps[0][1]<70+side/2 or ps[0][1]>370-side/2:
            print("Game Over!")
            self.game_over()
    def cheak_snake_eat_body(self):
        if self.position_of_snake[0] in self.position_of_snake[1:]:
            self.game_over()
    def game_over(self):
        self.canvas.delete("all")
        border = canvas.create_rectangle(150,150,350,250, fill="#003333")
        show_score=canvas.create_text(250,200,font=("Purisa",18),text=("Game Over!\nYour score is %d"%self.score),fill="#FFFFFF")
        raise SystemExit
    def play(self):
        self.move_snake()
        self.canvas.after(300, self.play)
#    def run(self):
snake=Snake()
snake.random_food_snake()
snake.play()
tk.mainloop()
        
    
    

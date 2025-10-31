import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle
from R00Triangle import R00Triangle 


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='cyan2')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None
        self.plain = None
        self.bush = None
        self.line = None
        self.flag = None

        self.draw()

    def draw(self):
        self.sun = Circle(canvas=self.canvas, diameter=110, color="peach puff", fill="yellow", line=5)
        self.sun.move_horizontal(450)
        self.sun.move_vertical(-40)
        self.sun.make_visible()

        self.wall = Square(canvas=self.canvas, size=30, color="brown", fill="green", line=2)
        self.wall.move_horizontal(440)
        self.wall.move_vertical(-10)
        self.wall.make_visible()

        self.line = Rectangle(canvas=self.canvas, height=195, width=5, color="black", fill="gray", line=2)
        self.line.move_horizontal(440)
        self.line.move_vertical(-10)
        self.line.make_visible()



        # flag pole and flagbase
        self.line = Rectangle(canvas=self.canvas, height=200, width=5, color="black", fill="brown", line=2)
        self.line.move_horizontal(170)
        self.line.move_vertical(60)
        self.line.make_visible()

        self.window = Square(canvas=self.canvas, size=50, color="black", fill="sienna2", line=2)
        self.window.move_horizontal(150)
        self.window.move_vertical(250)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="black", fill="sienna2", line=2)
        self.window.move_horizontal(150)
        self.window.move_vertical(250)
        self.window.make_visible()

        self.flag = R00Triangle(canvas=self.canvas, height=35, width=-60, color="black", fill="black", line=2)
        self.flag.move_horizontal(250)
        self.flag.move_vertical(100)
        self.flag.make_visible()

        
        
        # Yoshi bush with spikes
        self.roof = Triangle(canvas=self.canvas, height=35, width=80, color="peach puff", fill="red", line=2)
        self.roof.move_horizontal(-10)
        self.roof.move_vertical(240)
        self.roof.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=35, width=80, color="peach puff", fill="red", line=2)
        self.roof.move_horizontal(-10)
        self.roof.move_vertical(280)
        self.roof.make_visible()

        self.bush = Circle(canvas=self.canvas, diameter=75, color="white", fill="white", line=1)
        self.bush.move_horizontal(115)
        self.bush.move_vertical(190)
        self.bush.make_visible()

        self.bush = Circle(canvas=self.canvas, diameter=80, color="green", fill="green", line=1)
        self.bush.move_horizontal(120)
        self.bush.move_vertical(170)
        self.bush.make_visible()

        self.line = Rectangle(canvas=self.canvas, height=195, width=70, color="green", fill="green", line=1)
        self.line.move_horizontal(25)
        self.line.move_vertical(190)
        self.line.make_visible()

        self.bush = Circle(canvas=self.canvas, diameter=110, color="white", fill="green", line=1)
        self.bush.move_horizontal(55)
        self.bush.move_vertical(120)
        self.bush.make_visible()

       




        self.plain = Rectangle(canvas=self.canvas, height=100, width=150, color="white", fill="sienna3", line=2)
        self.plain.move_horizontal(350)
        self.plain.move_vertical(90)
        self.plain.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="white", fill="sienna2", line=2)
        self.window.move_horizontal(350)
        self.window.move_vertical(60)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="white", fill="sienna2", line=2)
        self.window.move_horizontal(410)
        self.window.move_vertical(60)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="white", fill="sienna2", line=2)
        self.window.move_horizontal(470)
        self.window.move_vertical(60)
        self.window.make_visible()




        self.plain = Rectangle(canvas=self.canvas, height=100, width=270, color="black", fill="sienna3", line=2)
        self.plain.move_horizontal(300)
        self.plain.move_vertical(190)
        self.plain.make_visible()

        self.plain = Rectangle(canvas=self.canvas, height=70, width=1300, color="black", fill="seagreen2", line=2)
        self.plain.move_horizontal(-60)
        self.plain.move_vertical(290)
        self.plain.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="black", fill="sienna2", line=2)
        self.window.move_horizontal(300)
        self.window.move_vertical(160)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="black", fill="sienna2", line=2)
        self.window.move_horizontal(350)
        self.window.move_vertical(160)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="black", fill="sienna2", line=2)
        self.window.move_horizontal(410)
        self.window.move_vertical(160)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="black", fill="sienna2", line=2)
        self.window.move_horizontal(470)
        self.window.move_vertical(160)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="black", fill="sienna2", line=2)
        self.window.move_horizontal(515)
        self.window.move_vertical(160)
        self.window.make_visible()



       
        self.window = Square(canvas=self.canvas, size=63, color="black", fill="black", line=1)
        self.window.move_horizontal(400)
        self.window.move_vertical(230)
        self.window.make_visible()
        
        self.bush = Circle(canvas=self.canvas, diameter=70, color="black", fill="black", line=1)
        self.bush.move_horizontal(435)
        self.bush.move_vertical(208)
        self.bush.make_visible()

        




    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")

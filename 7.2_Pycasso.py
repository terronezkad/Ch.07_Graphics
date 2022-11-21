'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
arcade.open_window(800,600,"Kadin Terronez")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

point_set=((150,600),(300,600),(315,590),(315,570),(140,570),(140,590))
arcade.draw_polygon_filled(point_set,arcade.color.ASH_GREY)

arcade.draw_text("inbox (1200) - hermonm@",145,580,arcade.color.BLACK,11)
arcade.draw_circle_filled(25,580,10,arcade.color.RED)
arcade.draw_circle_filled(75,580,10,arcade.color.YELLOW)
arcade.draw_circle_filled(125,580,10,arcade.color.GREEN)

arcade.draw_rectangle_filled(400,560,800,20,arcade.color.GAINSBORO)

for i in range (0,800,40):
    arcade.draw_text("URL",i,555,arcade.color.BLACK)

arcade.draw_rectangle_filled(400,300,650,475,arcade.color.SILVER_SAND)
arcade.draw_rectangle_filled(400,275,650,455,arcade.color.WHITE_SMOKE)
arcade.draw_text("New Message",80,515,arcade.color.BLACK)
arcade.draw_text("To",80,480,arcade.color.BLACK)
arcade.draw_text("Subject",80,440,arcade.color.DARK_GRAY)
arcade.draw_text("Tim Carver",120,480,arcade.color.BLACK)
arcade.draw_text("Peace out",150,440,arcade.color.BLACK)
arcade.draw_line(80,460,720,460,arcade.color.DAVY_GREY)
arcade.draw_line(80,420,720,420,arcade.color.DAVY_GREY)
arcade.draw_text("I'm getting to old for this.",80,400,arcade.color.BLACK)
arcade.draw_ellipse_filled(175,75,150,40,arcade.color.BLUE)
arcade.draw_text("Send",140,67,arcade.color.WHITE,22)


#quote:im getting too old for this










arcade.finish_render()
arcade.run()



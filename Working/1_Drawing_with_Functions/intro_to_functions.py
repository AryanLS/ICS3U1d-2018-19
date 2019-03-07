import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud(x, y):
    arcade.draw_circle_filled(125 + x, 500 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(50 + x, 500 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(90 + x, 550 + y, 50, arcade.color.WHITE)

def draw_rolling_hills():
    arcade.draw_circle_filled(350, 250, 100, arcade.color.LIGHT_GREEN)
    arcade.draw_circle_filled(100, -100, 450, arcade.color.GREEN)
    arcade.draw_circle_filled(550, -100, 400, arcade.color.DARK_GREEN)

def draw_tree():
    arcade.draw_triangle_filled(100, 250, 150, 300, 200, 250, arcade.color.BLUE)
    arcade.draw_triangle_filled(100, 225, 150, 275, 200, 225, arcade.color.BLUE)
    arcade.draw_triangle_filled(100, 200, 150, 250, 200, 200, arcade.color.BLUE)
    arcade.draw_rectangle_filled(150, 188, 25, 25, arcade.color.BROWN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()

   # call your draw functions

    draw_cloud(0, 0)
    draw_cloud(250, 0)
    draw_rolling_hills()
    draw_tree()
    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud():
    arcade.draw_circle_filled(125, 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(50, 500, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(90, 550, 50, arcade.color.WHITE)

def draw_rolling_hills():
    arcade.draw_circle_filled(250, 50, 400, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled()
    arcade.draw_circle_filled()

def draw_tree():


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()

   # call your draw functions

    draw_cloud()
    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
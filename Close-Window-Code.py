# You Need To Import Arcade!
import arcade

class Example(arcade.Window):
  """Example For Close Window Code"""
  
  # I believe You Would Like To Press A Key To Turn Off The Example. 
  def on_key_press(self, key, modifiers):
        " Key Press"
        # Fullscreen Control
        if arcade.key.SPACE:
            arcade.close_window()
  # By The Way Only Use This Function If They Aren't Using Any Keys For Different Functions.

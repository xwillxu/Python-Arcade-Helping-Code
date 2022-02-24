# Let's Start With This Example

import arcade

class Example(arcade.Window):
  """Basic Example For Fullscreen Control"""
  
  def __init__(self):
    """Where The Fullscreen Control Is"""
    # By The Way You Need The self For The __init__
    
    # The Code For Fullscreen Control   
    self.set_fullscreen(not self.fullscreen)
    
# If You Want To Change From Fullscreen To Normal You Will Add This Code Below
  def 

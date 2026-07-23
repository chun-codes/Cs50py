import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
font_list=figlet.getFonts()

def fontname():
  if len(sys.argv) == 0:
    figlet.setFont(font=random.choice(font_list))
  if len(sys.argv) == 2:  
    if sys.argv[1] in ["-f","--font"] and sys.argv[2] in font_list:
        figlet.setFont(font=sys.argv[2])
    else:
      sys.exit("Invalid font")

  font_name=input("Input: ")
  print(figlet.renderText(font_name))

fontname()
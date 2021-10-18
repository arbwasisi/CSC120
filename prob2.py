def bound(color):
    
    if color < 0:
        color = 0
    elif color > 255:
        color = 255
    else:
        color = color
        
    return color

class Color:
    def __init__(self,r,g,b):
        self.r = bound(r)
        self.g = bound(g)
        self.b = bound(b)
    
    def __str__(self):
        return "rgb({},{},{})".format(self.r, self.g, self.b)
        
    def html_hex_color(self):
        return "#{:02X}{:02X}{:02X}".format(self.r, self.g, self.b)
        
    def get_rgb(self):
        return (self.r,self.g,self.b)
        
    def set_standard_color(self, name):
        if name.lower() == 'red':
            self.r = 255
            self.g = 0
            self.b = 0
        elif name.lower() == 'yellow':
            self.r = 255
            self.g = 255
            self.b = 0
        elif name.lower() == 'black':
            self.r = 0
            self.g = 0
            self.b = 0
        elif name.lower() == 'white':
            self.r = 255
            self.g = 255
            self.b = 255
        else:
            print('ERROR: Color.set_standard_color():\
             Invalid color name: {}'.format(name))
    def remove_red(self):
        self.r = 0
        
def main():        

    obj = Color(3,-5,270)
    obj.set_standard_color('PoR FaVoR')
    print(obj.html_hex_color())
if __name__ == "__main__":
    main()
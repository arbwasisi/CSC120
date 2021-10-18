import math

PIE = math.pi

class Ball:
    def __init__(self, color, material, diameter):
        self.color = color
        self.material = material
        self.diameter = diameter
        
    def __str__(self):
        return 'Ball(color={}, material={}, diameter={})'\
        .format(self.color, self.material, self.diameter)
    
    def __eq__(self, other):
        if str(self.color).lower() == str(other.color).lower():
            if str(self.material).lower() == str(other.material).lower():
                if self.diameter == other.diameter:
                    return True
        return False
        
    def get_color(self):
        return self.color
        
    def get_material(self):
        return self.material
        
    def get_diameter(self):
        return self.diameter
        
    def get_volume(self):
        return 4*PIE*(((self.diameter/2)**3)/3)
        
    def paint(self, new_color):
        self.color = new_color
        
    def bounce(self):
        if self.material.lower() == 'stone':
            print('Thud')
        else:
            print('Boing')

def main():            
    obj = Ball('mauve', 'stone', 10)
    obj2 = Ball('mauve', 'stone', 10)
    
    print(str(obj2))
    
if __name__ == "__main__":
    main()
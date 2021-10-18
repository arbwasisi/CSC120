class Simplest:
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    
    def __init__(self,first,second,third):
        self.first = first
        self.second = second
        self.third = third
        
    def get_first(self):
        return self.first
        
    def get_second(self):
        return self.second
        
    def get_third(self):
        return self.third
        
    def rotate(self):
        self.first, self.second, self.third  =\
        self.second, self.third, self.first
        
class Band:
    
    def __init__(self, singer):
        self.singer = singer
        self.drummer = None
        self.guitar_players = list()
        
    def get_singer(self):
        return self.singer
        
    def set_singer(self, new_singer):
        self.singer = new_singer  
        
    def get_drummer(self):
        return self.drummer
        
    def set_drummer(self, new_drummer):
        self.drummer = new_drummer
        
    def add_guitar(self, new_guitar):
        self.new_guitar = new_guitar
        self.guitar_players.append(self.new_guitar)

    def get_guitars(self):
        return self.guitar_players
        
    def play_music(self):
        if self.singer == 'Frank Sinatra':
            print("Do be do be do")
        elif self.singer == 'Kurt Cobain':
            print("bargle nawdle zouss")
        else:
            print("La la la")
            
        
        if self.drummer is not None:
            print("Bang bang bang!")
            
        for guitarist in self.guitar_players:
            print("Strum!")
       

def main():
    obj = Simplest(10,20,30)
    print(obj.c)
    
if __name__ == "__main__":
    main()
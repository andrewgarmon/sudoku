class Tile:
    def __init__(self, x, y, value = None):
        self.value = value
        self.x = x
        self.y = y
        self.possible_values = [1,2,3,4,5,6,7,8,9]
    
    def get_value(self):
        return self.value

    def get_position(self):
        return [self.x,self.y]

    def get_possible_values(self):
        return self.possible_values

    def is_revealed(self):
        return bool(self.value)

        #have to find a way to return a reference to the block it is a part of

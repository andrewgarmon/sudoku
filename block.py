import tile
class block:

    def __init__(self, tiles = [None]):
        self.tiles = tiles
        self.revealed_tiles = [None]
        if tiles is not None:
            for i in range (1,10):
                if tiles[i].value in range(1,10):
                    self.revealed_tiles.append(tiles[i].value)
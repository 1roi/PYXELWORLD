import json
import os

from settings import *


class Saving(object):
    def __init__(self):
        # Dict of blocks that can be saved and loaded
        # Will be modified later, cause it's not the best solution
        self.saveDict = { str(GRASS):'GRASS', str(SAND):'SAND', str(BRICK):'BRICK', str(STONE):'STONE', str(WOODEN_PLANKS):"WOODEN_PLANKS", str(STONE_BRICKS):"STONE_BRICKS", str(COBBLESTONE):"COBBLESTONE"}
        self.loadDict = { 'GRASS': GRASS, 'SAND': SAND, 'BRICK': BRICK, 'STONE': STONE, 'WOODEN_PLANKS':WOODEN_PLANKS, 'COBBLESTONE':COBBLESTONE, 'STONE_BRICKS': STONE_BRICKS}

        # The file that will be used to save and load worlds
        self.saveFile = 'save.sav'

    def saveFileExists(self):
        """ Checks if the save file exists """
        if os.path.exists(self.saveFile) == True:
            return True
        else:
            return False
        
    def loadWorld(self, model):
        """ Loads the saved world in the file """
        fh = open(self.saveFile, 'r')
        worldMod = fh.read()
        fh.close()

        worldMod = worldMod.split('\n')

        for blockLine in worldMod:
            if blockLine != '':
                coords, blockType = blockLine.split('=>')
                model.add_block( tuple(json.loads(coords)), self.loadDict[blockType], False )
        
        print('World has been loaded')
    
    def saveWorld(self, model):
        """ Write all the blocks by it's type and position and put it all together in the save file with JSON """
        fh = open(self.saveFile, 'w')
        worldString = ''

        for block in model.world:
            worldString += json.dumps(block) + "=>" + self.saveDict[str(model.world[block])] + "\n"

        fh.write(worldString)
        fh.close()    
        print("World save completed")
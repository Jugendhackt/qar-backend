from random import * 
from mcpi.minecraft import Minecraft 
from mcpi import block 

import time
import sys
sys.setrecursionlimit(5000)
mc = Minecraft.create("localhost",25565) 
ids = mc.getPlayerEntityIds() 


class Maker():
    a,b,c = mc.entity.getTilePos(ids[0]) 
    print(a,b,c)
    def __init__(self,mwx,mwy,mwz): 
        self.mwx= mwx 
        self.mwy= mwy 
        self.mwz = mwz 
        self.feld=[]
        self.glass_house()
    def lab(self,dire,x,y,d,dires,n): 
            if x>= n-1 or y>= n-1 or y<=0 or x<=0: 
                return 
            count = -4 
            if self.feld [x][y]==0: 
                count =0 
            if self.feld[x+1][y]==0: 
                count+=1 
            if self.feld [x-1][y]==0: 
                count+=1 
            if self.feld[x][y+1]==0: 
                count+=1 
            if self.feld [x][y-1]==0: 
                count+=1 
                 
            if count<3: 
                return 
            self.feld[x][y]=1 
            mc.setBlock(x+self.mwx,1+self.mwz,y+self.mwy,block.AIR.id) 
            mc.setBlock(x+self.mwx,self.mwz-1,y+self.mwy,block.AIR.id) 
            mc.setBlock(x+self.mwx,self.mwz+2,y+self.mwy,block.AIR.id) 
            mc.setBlock(x+self.mwx,self.mwz-2,y+self.mwy,block.AIR.id) 
            mc.setBlock(x+self.mwx,self.mwz-3,y+self.mwy,block.AIR.id) 
            time.sleep(1/(len(self.feld))**2) 
             
                     
            while False in dires: 
                k =randint(0,3) 
             
                 
                dires[k]=True 
                if k ==0: 
                    x1=x 
                    y1=y+1 
                if k == 1: 
                    x1=x 
                    y1=y-1 
                if k ==2: 
                    x1=x-1 
                    y1=y 
                if k ==3: 
                    x1=x +1 
                    y1=y 
                self.lab(k,x1,y1,d+1,[False,False,False,False],n) 
             

    def make_w(self, size): 
        self.feld =[] 
        l =[] 
        for x in range(size): 
            l.append(0) 
        for x in range(size): 
            self.feld.append(list(l)) 
        return self.feld 
    def build_feld(self,s): 
            mc.setBlocks(self.mwx-5,self.mwz-8,self.mwy-5,s+self.mwx-1,self.mwz-1,s+self.mwy+5,block.STONE.id)#replace 
#to some other block 
    def glass_house(self):
        mc.setBlocks(self.mwx+10,self.mwy+10,self.mwz+10,self.mwx+13,self.mwy+13,self.mwz+13,block.GLASS.id) 
        mc.setBlocks(self.mwx+11,self.mwy+11,self.mwz+11,self.mwx+12,self.mwy+12,self.mwz+12,block.AIR.id) 
    def main(self,s): 

        self.feld = self.make_w(s)
        self.build_feld(s)
        self.lab(1,1,1,1,[False,False,False,False],s) 
        for kk in range(s): 
            if self.feld[-2][s-kk-1]!=0: 
                self.feld[-1][s-kk-1]="E" 
                x= s-kk-1 
                y= s-1 
                mc.setBlock(x+self.mwx,self.mwz-1,y+self.mwy,block.WOOL.id,5) 
                mc.setBlock(x+self.mwx,self.mwz-2,y+self.mwy,block.WOOL.id,5) 
                time.sleep(1/30) 
                mc.setBlock(x+self.mwx,self.mwz-3,y+self.mwy,block.WOOL.id,5) 
                mc.setBlock(x+self.mwx,self.mwz-4,y+self.mwy-1,block.WOOL.id,5) 
                break 
        self.feld[0][1]="A" 
        mc.setBlock(self.mwx+1,self.mwz-1,self.mwy,block.WOOL.id,3) 
        mc.setBlock(self.mwx+1,self.mwz-2,self.mwy,block.WOOL.id,3) 
        time.sleep(1/30) 
        mc.setBlock(self.mwx+1,self.mwz-3,self.mwy,block.WOOL.id,3) 
        mc.setBlock(self.mwx,self.mwz-1,self.mwy+1,block.WOOL.id,3) 
        time.sleep(1/30) 
        mc.setBlock(self.mwx,self.mwz-2,self.mwy+1,block.WOOL.id,3) 
        mc.setBlock(self.mwx,self.mwz-3,self.mwy+1,block.WOOL.id,3) 
        time.sleep(1/30) 
        #mc.setBlock(self.mwx,self.mwz,self.mwy,block.WOOL.id,3) 
        mc.setBlock(self.mwx+1,self.mwz-4,self.mwy+1,block.WOOL.id,3) 

            #x= s-kk-1 
            #y= s-1 
        time.sleep(1) 
        mc.player.setPos(self.mwx+1.5,self.mwz-3,self.mwy+1.5) 

mc.setBlocks(2,-20,-117,32,10,-72,block.STONE.id) 
#spawnpoint setzen
mc.player.setPos(10,-15,-100) 
#leerer Raum 
mc.setBlocks(7,-15,-107,22,-10,-92,block.AIR.id) 
#Fackeln  
mc.setBlocks(7,-12,-107,7,-12,-92,block.TORCH.id) 
mc.setBlocks(22,-12,-107,22,-12,-92,block.TORCH.id) 
mc.setBlocks(7,-12,-107,22,-12,-107,block.TORCH.id) 
mc.setBlocks(7,-12,-92,22,-12,-92,block.TORCH.id) 
#Tor 1 
mc.setBlocks(22,-15,-104,22,-13,-104,block.SAND.id) 
mc.setBlocks(22,-15,-102,22,-13,-102,block.SAND.id) 
#Spawn point 
mc.setBlock(9,-16,-100,block.WOOL.id,1) 
 
mc.setBlock(19,-16,-106,block.SAND.id) 
mc.setBlock(21,-16,-104,block.SAND.id) 
mc.setBlock(18,-16,-106,block.SAND.id) 
    
mc.setBlocks(22,-15,-107,22,-13,-107,block.SAND.id) 
mc.setBlocks(21,-15,-107,21,-14,-107,block.SAND.id)
mc.setBlocks(22,-15,-106,22,-14,-106,block.SAND.id) 
mc.setBlock(20,-15,-107,block.SAND.id) 
mc.setBlock(22,-15,-105,block.SAND.id) 
mc.setBlock(21,-15,-106,block.SAND.id)
mc.setBlocks(18,-16,-103,22,-16,-107,block.SAND.id) 
mc.setBlocks(18,-15,-106,18,-13,-106,block.CACTUS.id)
print(block.WATER_STATIONARY.id)
mc.setBlock(21,-15,-104,32) 
mc.setBlock(22,-14,-105,32)
mc.setBlock(21,-13,-107,32) 
mc.setBlocks(19,-16,-104,20,-16,-105,block.WATER_STATIONARY.id)
mc.setBlock(20,-16,-106,block.WATER_STATIONARY.id)
mc.setBlock(21,-16,-105,block.WATER_STATIONARY.id)





g=False
mwx = -30
mwy = 0
mwz = 50
while True: 
     
     
    a,b,c = mc.entity.getTilePos(ids[0]) 
    print(a,b,c)
    if g:
        if not blk.id == block.WOOL.id:
            mc.setBlock(a,mwz-4,c,block.WOOL.id,3)
    blk = mc.getBlockWithData(a,b-1,c) 
    if blk.id == block.WOOL.id and blk.data == 5: 
        mc.player.setPos(10,-15,-100) 
        mc.postToChat("Gratulation :)") 
        g=False
    if [a,b,c]== [22,-15,-103]: 
        
        #teleportieren
        maker = Maker(mwx,mwy,mwz)
        g=True
        mc.player.setPos(mwx+12,mwy+12,mwz+12)
        print("hi")
        a,b,c = mc.entity.getTilePos(ids[0]) 
        print(a,b,c)
        maker.main(90)
        print("lol")
    elif [a,b,c] == [1,1,1]:
        pass

from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello')

x, y = -30, 80
for w in range(10):
    z = -30
    for v in range(10):
        mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
        sleep(0.5)
        z += 1
    x += 1
mc.postToChat('Floor')


from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #2  golden column')

# x, z = 24, 24
# y = param.Y_SEA + 1
# for _i in range(10):
#     mc.setBlock(x, y, z,  param.GOLD_BLOCK)
#     sleep(0.25)
#     y += 2

x, y, z = 22, 98, 22
for i in range(10):
    mc.setBlock(x, y, z,  param.GOLD_BLOCK)
    sleep(2)
    y += 2

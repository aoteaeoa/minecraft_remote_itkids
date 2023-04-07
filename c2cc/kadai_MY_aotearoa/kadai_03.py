from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #3  seven columns')

# x = 5
# z = 10
# for _n in range(7):
#     y = param.Y_SEA + 1
#     for _i in range(10):
#         mc.setBlock(x, y, z,  param.IRON_BLOCK)
#         sleep(0.25)
#         y += 1
#     x += 2

x, z = 25, 25
for i in range(7):
    y = 100
    for n in range(10):
       mc.setBlock(x, y, z,  param.SEA_LANTERN_BLOCK)
       sleep(2)
       y += 1
    x += 2

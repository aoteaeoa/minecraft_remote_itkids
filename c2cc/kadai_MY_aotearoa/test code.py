from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello')

# x, y = -30, 80
# for w in range(10):
#     z = -30
#     for v in range(10):
#         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
#         sleep(0.5)
#         z += 1
#     x += 1
# mc.postToChat('Floor')

# def setPyramid(mc=mc, x=-30, y= 100, z=-30, size=3, blockTypeId=param.SEA_LANTERN_BLOCK):
#     while size > 0:
#         mc.setBlocks(x, y, z,  x + size-1, y, z + size -1, blockTypeId)
#         x += 1
#         z += 1
#         size -= 2
#         y += 1
#         sleep(0.3)

# if __name__ == "__main__":
#     mc = Minecraft.create(port=param.PORT_MC)
#     mc.postToChat('kadai #8  pyramids ')
#     sleep(1)
#     setPyramid(x=-70, z=-70, y=200, size=15)

# x, y, z = 30, 200, 50
# size = 10
# mc.setBlocks(x, y, z, x + size -1, y - size + 5, z + size -1, param.GLOWSTONE)
# while size > 1:
#     mc.setBlocks(x, y, z, x + size -1, y, z + size -1, param.GLOWSTONE)
#     mc.setBlock(x, y, z, param.AIR)
#     mc.setBlock(x + size -1, y, z, param.AIR)
#     mc.setBlock(x + size -1, y, z + size -1, param.AIR)
#     mc.setBlock(x, y, z + size -1, param.AIR)
#     x += 1
#     z += 1
#     size -= 2
#     y += 1
#     sleep(0.1)
# x, y, z = 30, 200, 50
# size = 10
# while size > 1:
#     mc.setBlocks(x, y - 5, z, x + size -1, y - 5, z + size -1, param.GLOWSTONE)
#     mc.setBlock(x, y -5, z, param.AIR)
#     mc.setBlock(x + size -1, y -5 , z, param.AIR)
#     mc.setBlock(x + size -1, y -5 , z + size -1, param.AIR)
#     mc.setBlock(x, y - 5, z + size -1, param.AIR)
#     x += 1
#     z += 1
#     size -= 2
#     y -= 1
#     sleep(0.1)

x0, y0, z0 = 570, 125, 400

z = z0 + 2
for o in range(2):
    x =x0 + 2
    for p in range(2):
        y = y0 + 1
        for q in range(5):
            mc.setBlock(x, y, z, param.GLOWSTONE)
            sleep(0.5)
            y += 1
        x += 5
    z += 5
mc.postToChat('4 columns')

x = x0
y = y0
z = z0
size = 10
while size > 1:
    mc.setBlocks(x, y, z, x + size -1, y, z + size -1, param.GLOWSTONE)
    mc.setBlock(x, y, z, param.AIR)
    mc.setBlock(x + size -1, y, z, param.AIR)
    mc.setBlock(x + size -1, y, z + size -1, param.AIR)
    mc.setBlock(x, y, z + size -1, param.AIR)
    x += 1
    z += 1
    size -= 2
    y -= 1
    sleep(0.3)
mc.postToChat('Hemisphere')


x = x0
y = y0 + 5
z = z0
size = 10
while size > 1:
    mc.setBlocks(x, y, z, x + size -1, y, z + size -1, param.GLOWSTONE)
    mc.setBlock(x, y, z, param.AIR)
    mc.setBlock(x + size -1, y, z, param.AIR)
    mc.setBlock(x + size -1, y, z + size -1, param.AIR)
    mc.setBlock(x, y, z + size -1, param.AIR)
    x += 1
    z += 1
    size -= 2
    y += 1
    sleep(0.3)
mc.postToChat('Roof')

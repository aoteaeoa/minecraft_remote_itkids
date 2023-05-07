from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello')

x0, y0, z0 = 600, 120, 400

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
    y += 1
    sleep(0.3)

x = x0
y = y0
z = z0
size = 10
mc.setBlocks(x, y, z, x + size -1, y - 3, z + size -1, param.GLOWSTONE)
y = y0 - 4
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
mc.postToChat('first Dango')

x = x0
y = y0 - 13
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

x = x0
y = y0 - 13
z = z0
size = 10
mc.setBlocks(x, y, z, x + size -1, y - 3, z + size -1, param.GLOWSTONE)
y = y0 - 17
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
mc.postToChat('Second Dango')

x = x0
y = y0 - 26
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

x = x0
y = y0 - 26
z = z0
size = 10
mc.setBlocks(x, y, z, x + size -1, y - 3, z + size -1, param.GLOWSTONE)
y = y0 - 30
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
mc.postToChat('third Dango')

mc.setBlocks(x0 + 5, y0 - 50, z0 + 5, x0 + 5, y0 + 10, z0 + 5, param.GLOWSTONE)

mc.postToChat('Bon appetit!!')

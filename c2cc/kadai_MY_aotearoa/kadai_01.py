from mcje.minecraft import Minecraft
import param_MCJE as param


mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #1  the first golden block')

mc.setBlock(20, 75, 20,  param.GOLD_BLOCK)

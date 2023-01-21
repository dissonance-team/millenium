import millenium, time

driver = millenium.millenium(port=2741)

theMinecraft = driver.getMinecraft()
thePlayer = theMinecraft.getPlayer()

while True:
    velY = float(thePlayer.getFishHook().getVelocityY())
    velX = float(thePlayer.getFishHook().getVelocityX())
    velZ = float(thePlayer.getFishHook().getVelocityZ())

    if (velY < -0.05 and velX == 0 and velZ == 0 ):
        theMinecraft.getInteractionManager().interactItem()

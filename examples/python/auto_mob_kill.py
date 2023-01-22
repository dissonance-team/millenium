import millenium, time

driver = millenium.millenium(port=2741)

theMinecraft = driver.getMinecraft()
thePlayer = theMinecraft.getPlayer()
raycast = theMinecraft.getRayCast()

while True:
    if (raycast.isEntityHit() and thePlayer.getAttackCooldown() == 1.0):
        thePlayer.swingSword()
    time.sleep(0.25)

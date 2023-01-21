<h1 align="center">
  <br>
  Millenium
  <br>
</h1>

Millenium - like [selenium](https://github.com/SeleniumHQ/selenium), but for [Minecraft Fabric](https://github.com/FabricMC/fabric). Automate your Minecraft gameplay! Currently under development.

![Issues](https://img.shields.io/github/issues/Maxdsdsdsd/millenium)
![License](https://img.shields.io/github/license/Maxdsdsdsd/millenium)

## Client Code Example

### AutoFish:

```bash
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
```

<img src="https://user-images.githubusercontent.com/33353036/213884466-5af7cc35-69f5-4760-a1bf-be4627cd6616.gif" width="550" height="300"/>

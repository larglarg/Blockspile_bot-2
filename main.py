import configparser
from mcpi.minecraft import Minecraft
from time import sleep

# Konfigurationsdatei lesen
config = configparser.ConfigParser()
config.read('config.ini')
username = config.get('Minecraft', 'username')
password = config.get('Minecraft', 'password')

# Verbindung zum Minecraft-Server herstellen
mc = Minecraft.create("colorcraft.larglarg.com")



# "/warp xp_farm" in den Chat senden
mc.postToChat("/warp xp_farm")

# Warten, bis die Spieler-Chat-Nachricht angezeigt wird
while True:
    chat_events = mc.events.pollChatPosts()
    if chat_events:
        for chat_event in chat_events:
            if chat_event.message == "/warp xp_farm":
                break
        break
    sleep(0.1)



# Zuschlagen



# Essen, wenn vier Hungerbalken fehlen
while True:
    # Einen Block nach rechts laufen
    mc.player.setPos(mc.player.getPos().x + 1, mc.player.getPos().y, mc.player.getPos().z)

    # Einen Block nach links laufen
    mc.player.setPos(mc.player.getPos().x - 1, mc.player.getPos().y, mc.player.getPos().z)
    mc.player.inventory.selected_item = 0
    mc.player.hitBlock(mc.player.getPos().x, mc.player.getPos().y, mc.player.getPos().z)
    # Auf den Slot 1 wechseln

    if mc.player.getHunger() < 16 - 4:
        mc.player.setSlot(8)
        mc.postToChat("Eating...")
        mc.player.consumeItem()
        sleep(0.5)
    else:
        break

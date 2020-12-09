class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False

    def turnOn(self):
        if self.on == False:
            self.on = True
        else:
            print ("TV is already On")

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        self.channel = channel

    def getVolumne(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

    def volumeUp(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print ("Maximum volume reached")

    def volumeDown(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print ("Already MUTE!!")

    def channelUp(self):
        if self.channel <= 100:
            self.channel += 1
        else:
            print ("No more channels!")

    def channelDown(self):
        if self.channel > 0:
            self.channel += 1
        else:
            print ("Already at the bottom channel")



tv1 = TV()

tv1.turnOn()
tv1.setChannel(30)
tv1.channelUp()

print ("TV Channel = ", tv1.channel)

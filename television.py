class Television:
    """A class representing Television status"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status, muted, volume, channel):
        """
        Television variables
        :param status: Television ON or OFF
        :param muted: Television volume ON or OFF
        :param volume: Television volume level MIN or MAX
        :param channel: Television channel MIN or MAX
        """
        self.status = status
        self.muted = muted
        self.volume = volume
        self.channel = channel

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


#All the instance variables should be private.

    def power(self):
        """
        To determine Television is ON or OFF
        :return: True or False
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def mute(self):
        """
        To determine Television Volume is Muted or not Muted
        :return: True or False
        """
        if self.__status:
            self.__muted = False
            self.__volume = Television.MIN_VOLUME
        else:
            self.__muted = True
            self.__volume = Television.MAX_VOLUME

    def channel_up(self):
        """
        To determine if the channel needs to increase
        :return: Minimum channel
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        """
        This should be used to decrease the tv channel value
        :return: maximum channel
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

# TODO: Still not getting the right volume in the Main.py program
# TODO: Will continue to troubleshoot the on going failure.

    def volume_up(self):
        """
        This should be used to increase the tv volume value
        :return: Max volume
        """
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                return
            else:
                return Television.MAX_VOLUME

    def volume_down(self):
        """
        This should be used to decrease the tv volume value
        :return: MIN Volume
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                return
            else:
                return Television.MIN_VOLUME

    def __str__(self):
        """
        This should send the values to the main.py
        :return: values
        """

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'









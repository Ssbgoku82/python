class Television:
    """A class representing Television status"""
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize the Television status

        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


#All the instance variables should be private.

    def power(self) -> None:
        """
        To determine Television is ON or OFF
        :return: True or False
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def mute(self) -> None:
        """
        To determine Television Volume is Muted or not Muted
        :return: True or False
        """
        if not self.__status:
            return
        if self.__muted:
            self.__muted = False
        else:
            self.__muted = True

    def channel_up(self) ->None:
        """
        To determine if the channel needs to increase
        :return: Minimum channel
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) ->None:
        """
        This should be used to decrease the tv channel value
        :return: maximum channel
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)



    def volume_up(self) ->None:
        """
        This should be used to increase the tv volume value
        :return: Max volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) ->None:
        """
        This should be used to decrease the tv volume value
        :return: MIN Volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This should send the values to the main.py
        :return: values
        """
        volume_display = "On Mute" if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'









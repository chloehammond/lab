class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        pass

    def power(self):
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False
        pass

    def channel_up(self):
        if self.__status is True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            elif self.__channel >= Television.MIN_CHANNEL:
                self.__channel += 1
        pass

    def channel_down(self):
        if self.__status is True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
        pass

    def volume_up(self):
        if self.__status is True:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            elif self.__volume >= Television.MIN_VOLUME:
                self.__volume += 1
        pass

    def volume_down(self):
        if self.__status is True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            elif self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
        pass

    def __str__(self):
        if self.__status is True:
            return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        elif self.__status is False:
            return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        pass

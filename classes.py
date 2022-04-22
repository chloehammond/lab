class Television:
    '''
    Class to represent the television objects
    '''
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        '''
        Method to set the default state of the tv
        '''
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False
        pass

    def power(self):
        '''
        Method to turn the tv on and off
        '''
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False
        pass

    def channel_up(self):
        '''
        Method to turn the channel up
        '''
        if self.__status is True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            elif self.__channel >= Television.MIN_CHANNEL:
                self.__channel += 1
        pass

    def channel_down(self):
        '''
        Method to turn the channel down
        '''
        if self.__status is True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
        pass

    def volume_up(self):
        '''
        Method to turn the volume up
        '''
        if self.__status is True:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            elif self.__volume >= Television.MIN_VOLUME:
                self.__volume += 1
        pass

    def volume_down(self):
        '''
        Method to turn the volume down
        '''
        if self.__status is True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            elif self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
        pass

    def __str__(self):
        '''
        Method to relay the status of the tv
        :return: The current status of each object of the tv
        '''
        if self.__status is True:
            return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        elif self.__status is False:
            return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        pass

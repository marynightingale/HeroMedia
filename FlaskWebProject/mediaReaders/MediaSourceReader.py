from abc import ABCMeta, abstractmethod


class MediaSourceReader:
    __metaclass__ = ABCMeta


    @abstractmethod
    def getLatestPosts(self, count):
        pass

from abc import ABCMeta, abstractmethod


class MediaSourceReader(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def getLatestPosts(self, count=1):
        pass

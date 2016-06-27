from MediaSourceReader import MediaSourceReader
from IGClientFacade import IGClientFacade
import ReaderResources as R


class IGReader(MediaSourceReader):
    def __init__(self):
        self.config = {
            R.IGCONFIG_CLIENT_ID: 'b3e2bf83b14747e89cb526adf934563c',
            R.IGCONFIG_CLIENT_SECRET: '7855bdc2ae4341468784204895aaa0a6',
            R.IGCONFIG_ACCESS_TOEKN: '189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
            R.IGCONFIG_USER_ID: '189464193'
        }
        self.IGClient = IGClientFacade(self.config)

    def getLatestPosts(self, count=1):
        if count < 1:
            raise ValueError("IGReader.getLastestPost: attribute COUNT must be >1. Got {}".format(count))

        posts, next_ = self.IGClient.getMediaOfUser(count=count, max_id="0")

        return posts

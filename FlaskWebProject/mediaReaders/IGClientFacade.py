from instagram.client import InstagramAPI
import ReaderResources as R


class IGClientFacade:
    def __init__(self, config):
        if R.IGCONFIG_CLIENT_ID \
                and R.IGCONFIG_CLIENT_SECRET \
                and R.IGCONFIG_ACCESS_TOEKN \
                and R.IGCONFIG_USER_ID in config:
            self.access_token = config[R.IGCONFIG_ACCESS_TOEKN]
            self.client_id = config[R.IGCONFIG_CLIENT_ID]
            self.client_secret = config[R.IGCONFIG_CLIENT_SECRET]
            self.user_id = config[R.IGCONFIG_USER_ID]
        else:
            raise ValueError("IGClientFacade.__init__: CONFIG did not contain all required value")

        self.api = InstagramAPI(access_token=self.access_token, client_secret=self.client_secret,
                                client_id=self.client_id)

    def getMediaByTag(self, tag, count=1, max_tag_id="0"):
        return self.api.tag_recent_media(count=count, tag_name=tag, max_tag_id=max_tag_id)

    def getMediaOfUser(self, count=1, max_id="0"):
        if count < 1:
            raise ValueError("IGClientFacade.getMediaOfUser: attribute COUNT must be >1. Got {}".format(count))
        if not isinstance(max_id, basestring):
            raise TypeError("IGClientFacade.getMediaOfUser: MAX_ID must be a string")

        try:
            return self.api.user_recent_media(user_id=self.user_id, count=count, max_id=max_id)
        except:
            raise Exception("IGClientFacade.getMediaOfUser: Instagram API call failed")

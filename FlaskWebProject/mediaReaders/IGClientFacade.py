from instagram.client import InstagramAPI


class IGClientFacade:
    def __init__(self, config):
        self.access_token = config["access_token"]
        self.client_id = config["client_id"]
        self.client_secret = config["client_secret"]
        self.redirect_url = config["redirect_url"]
        self.api = InstagramAPI(access_token=self.access_token, client_secret=self.client_secret,
                                client_id=self.client_id)

    def getMediaByTag(self, tag, count=1):
        return self.api.tag_recent_media(count=count, tag_name=tag)

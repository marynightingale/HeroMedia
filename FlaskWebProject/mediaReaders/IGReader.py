from instagram.client import InstagramAPI

config = {
    'clientId': 'b3e2bf83b14747e89cb526adf934563c',
    'clientSecret': '7855bdc2ae4341468784204895aaa0a6',
    'accessToken': '189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e'
}

access_token = config['accessToken']
client_secret = config['clientSecret']
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.tag_recent_media(count=1, max_tag_id="0", tag_name="paleo")
for media in recent_media:
    print media.caption.text

api = InstagramAPI(client_id=config['clientId'], client_secret=config['clientSecret'])
popular_media = api.media_popular(count=5)
for media in popular_media:
    print media.images['standard_resolution'].url

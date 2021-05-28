from requests_oauthlib import OAuth1Session


def make_oauth_session(
    api_key: str, api_secret: str, access_token: str, access_token_secret: str
):
    return OAuth1Session(
        api_key,
        api_secret,
        access_token,
        access_token_secret,
    )

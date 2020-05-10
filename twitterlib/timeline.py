import auth


credentials = auth.get_credentials()
token = auth.app_access_token(**credentials)
api = auth.setup_api(token)

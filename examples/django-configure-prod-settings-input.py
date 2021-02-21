from decouple import config
ALLOWED_HOSTS = [config("ALLOWED_HOSTS")]
SITE_ID = config('SITE_ID')
DEBUG = config('DEBUG', default=False, cast=bool)


# in a seperate file called .env :
#  ALLOWED_HOSTS='https://stum.io'
#  SITE_ID = 1
#  DEBUG=False

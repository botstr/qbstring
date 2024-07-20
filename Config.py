import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = "a210a03b44f18af854e887d69e287b70"
    BOT_TOKEN = "7422272168:AAFS3dqaypMTPvnbV7UNhBYyOIuqxl9dBjE"
    DATABASE_URL = "postgresql://mohamed_i0v5_user:xCYCroyJR5nFAlEwhFeMXSUCxcK5NmTO@dpg-cqbfmgjv2p9s73eqop2g-a.frankfurt-postgres.render.com/mohamed_i0v5"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "Scorpions_scorp"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

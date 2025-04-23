import dotenv, os
from os.path import abspath, exists, join

def execute():
    try:
        ENV_PATH = abspath(join(__file__, "..", "..", ".env"))
        MIGRATIONS_PATH = abspath(join(__file__, "..", "migrations"))

        if exists(path = ENV_PATH):
            dotenv.load_dotenv(dotenv_path= ENV_PATH)

        if not exists(MIGRATIONS_PATH):
            os.system(os.environ["DB_INIT"])

        os.system(os.environ["DB_MIGRATE"])
        os.system(os.environ["DB_UPGRADE"])
    except Exception as error:
        print(error)
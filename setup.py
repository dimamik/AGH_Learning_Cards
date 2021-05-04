import logging
import subprocess


def migrate_and_upgrade():
    logging.info("Performing update and migrate on database")

    subprocess.call("python ./app/database/manage/manage.py db migrate", shell=True)

    subprocess.call("python ./app/database/manage/manage.py db upgrade", shell=True)


if __name__ == '__main__':
    migrate_and_upgrade()

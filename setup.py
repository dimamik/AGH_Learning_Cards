import subprocess


def migrate_and_upgrade():
    subprocess.call("python ./database/manage/manage.py db migrate", shell=True)

    subprocess.call("python ./database/manage/manage.py db upgrade", shell=True)


if __name__ == '__main__':
    migrate_and_upgrade()

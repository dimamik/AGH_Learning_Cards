from flask import Flask

from database.models.database_init import init_database_with_app
from env import POSTGRES
from logic.contexts.user_context import UserContext

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

init_database_with_app(app)


@app.route('/')
def hello_world():
    # UserContext.add_new_user('username', 'password')
    u_inst = UserContext.get_user_instance_by_username('username')
    # u_inst.set_user_info('New Description')
    # print(u_inst.change_password('password', 'new_password'))

    # print(u_inst.user.cards)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

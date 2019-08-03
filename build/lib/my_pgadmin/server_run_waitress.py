""" Running pgAdmin4 under windows with waitress.

wheel download from here:
https://www.pgadmin.org/download/
    # there is a problem with flask v>=1, had to downgrade

    Requirements flask==0.12.4 flask_babel flask_htmlmin flask_login flask_security
    flask_paranoid py-dateutil flask_sqlalchemy flask_gravatar flask_migrate
    simplejson pycryptodome psycopg2 sqlparse waitress
"""



from waitress import serve
from pgadmin4 import pgAdmin4

def run():
    serve(pgAdmin4.app, listen='*:8081')


if __name__ == "__main__":
    run()    
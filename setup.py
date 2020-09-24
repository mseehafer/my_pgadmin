from setuptools import setup

setup(name='my_pgadmin',
      version='0.1',
      description='pgadmin server based on waitress',
      # url='https://bitbucket.org/me/my_package',
      packages=['my_pgadmin'],
      install_requires=[
          "flask",
          "flask_babel",
          "flask_htmlmin",
          "flask_login",
          "flask_security",
          "flask_paranoid",
          "py-dateutil",
          "flask_sqlalchemy",
          "flask_gravatar",
          "flask_migrate",
          "simplejson",
          "pycryptodome",
          "psycopg2",
          "sqlparse",
          "waitress"
          # ,
          # 'pgadmin4 @ https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.11/pip/pgadmin4-4.11-py2.py3-none-any.whl'
      ],
      zip_safe=False)

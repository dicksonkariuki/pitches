from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch
from flask_migrate import Migrate,MigrateCommand


app = create_app('Production')


migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('runserver',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def add_shell():
  return{"db":db,"User":User,"Pitch":Pitch}

@manager.command
def test():
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestResult(verbosity=5).run(tests)

if __name__=='__main__':
  manager.run()
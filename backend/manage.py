#coding:utf-8
import sys
import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import db, app
from app.models import User, PGoal


manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(
        app = app,
        db = db,
        User = User,
        PGoal = PGoal
    )

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def createdb():
    db.create_all()

@manager.command
def test():
    import unittest
    tests = unittest.Testloader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

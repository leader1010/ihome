from flask_migrate import Migrate, MigrateCommand
from ihome_business import create_app, db
from flask_script import Manager

app = create_app("dev")

# 创建管理工具对象
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()

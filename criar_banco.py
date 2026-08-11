from newsite import database, app

from newsite.models import Usuario, Foto

with app.app_context():
    database.create_all()
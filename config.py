import bcrypt
from routes.invoice_registration import invoice_registration_route
from database.database import db
from models.invoice_registration import InvoiceRegistration
from models.user import User
from routes.login_page import login_route

def configure_all(app):
    configure_routes(app)
    configure_db()
    
def configure_routes(app):
    app.register_blueprint(invoice_registration_route, url_prefix="/invoice")
    app.register_blueprint(login_route, url_prefix="/login")

def configure_db():
    if db.is_closed():
        db.connect()
        db.create_tables([InvoiceRegistration, User])
        if User.select().count() == 0:
            original_password = bcrypt.hashpw("senha123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            User.create(name="João Silva", email="joao@mercado.com.br", password=original_password)
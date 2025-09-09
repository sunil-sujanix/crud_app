from flask import Flask
from routes import routes_bp
from flask_cors import CORS
from config import Config
from models import Tasks,db
from flask_migrate import Migrate


app=Flask(__name__)
app.config.from_object(Config)
CORS(app)


db.init_app(app)


migrate=Migrate(app,db)


app.register_blueprint(routes_bp)

if __name__=='__main__':
    app.run(debug=True)
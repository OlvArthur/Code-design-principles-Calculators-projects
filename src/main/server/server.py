from flask import Flask
from src.main.routes.calculators import calcs_routes_bp

app = Flask(__name__)

app.register_blueprint(calcs_routes_bp)
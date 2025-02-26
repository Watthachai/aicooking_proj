from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config  # Import the Config class
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load configuration from the Config class
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from app.routes.account_routes import account_bp
    app.register_blueprint(account_bp, url_prefix='/api/account')
    from app.routes.menu_routes import menu_bp
    app.register_blueprint(menu_bp, url_prefix='/api/menu')
    from app.routes.menutype_routes import menutype_bp
    app.register_blueprint(menutype_bp, url_prefix='/api/menutype')
    from app.routes.step_routes import step_bp
    app.register_blueprint(step_bp, url_prefix='/api/step')
    from app.routes.history_routes import history_bp
    app.register_blueprint(history_bp, url_prefix='/api/history')
    from app.routes.waste_routes import waste_bp
    app.register_blueprint(waste_bp, url_prefix='/api/waste')
    from app.routes.ingredients_routes import ingredients_bp
    app.register_blueprint(ingredients_bp, url_prefix='/api/ingredients')
    from app.routes.menuingredients_routes import menuingredients_bp
    app.register_blueprint(menuingredients_bp, url_prefix='/api/menuingredients')
    from app.routes.payment_routes import payment_bp
    app.register_blueprint(payment_bp, url_prefix='/api/payment')
    from app.routes.order_routes import order_bp
    app.register_blueprint(order_bp, url_prefix='/api/order')
    from app.routes.orderitem_routes import orderitem_bp
    app.register_blueprint(orderitem_bp, url_prefix='/api/orderitem')
    from app.routes.table_routes import table_bp
    app.register_blueprint(table_bp, url_prefix='/api/table')
    from app.routes.ingredientpack_route import ingredientpack_bp
    app.register_blueprint(ingredientpack_bp, url_prefix='/api/ingredientpacks')
    from app.routes.ingredientpackitems_route import ingredientpackitems_bp
    app.register_blueprint(ingredientpackitems_bp, url_prefix='/api/ingredientpackitems')
    from app.routes.menuingredientpack_route import menuingredientpack_bp
    app.register_blueprint(menuingredientpack_bp, url_prefix='/api/menuingredientpack')

    from app.tests.account_apitest_routes import account_apitest_bp
    app.register_blueprint(account_apitest_bp, url_prefix='/api/test/account')
    return app
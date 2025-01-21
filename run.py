from flask import Flask
from app.config import db  # Import the db object and model configurations
import app.config  # Ensure models are registered with SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary warnings

# Initialize the database with Flask app
db.init_app(app)

# Define a basic route for testing
@app.route('/')
def home():
    return "Welcome to the Examination Test App!"

if __name__ == '__main__':
    # Ensure the database schema is created before running the app
    with app.app_context():
        db.create_all()
        print("Database connected and initialized.")
    app.run(debug=True)

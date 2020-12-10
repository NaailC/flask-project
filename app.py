# Import app module
from application import app

# Run on current host
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")
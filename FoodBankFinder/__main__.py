from FoodBankFinder import *
from FoodBankFinder.controllers import *

FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT, host='0.0.0.0')

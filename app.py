#  Created by Bogdan Trif on 2022.05.24 , 11:52 AM ; btrif

from routes import index
from settings import *


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port = 7000, use_reloader=True)

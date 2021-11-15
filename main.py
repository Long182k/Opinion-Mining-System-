from init import app
from Controller.auth import *
from Controller.Posts import *
from Controller.Admin import *

#app.run(host='localhost', port=5000,debug = True, threaded = True, use_reloader = False)
app.run(host='0.0.0.0', port=5000,debug = True, threaded = True, use_reloader = False)

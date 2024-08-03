from flask import Flask
from models import storage
from api.v1.views import app_views
"""
this is the starting point of v1
"""

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext()
def handleTearDown():
  """
  handle teardown
  """
  storage.close()


if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5000,threaded=True)

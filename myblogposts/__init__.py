from flask import Flask

app = Flask(__name__)

from myblogposts.core.views import core
from myblogposts.error_pages.handlers import error_page

app.register_blueprint(core)
app.register_blueprint(error_page)
from flask import Blueprint, render_template

error_page = Blueprint("error", __name__)

@error_page.app_errorhandler(404)
def error_404(e):
    return render_template("error_pages/404.html"), 404

@error_page.app_errorhandler(403)
def error_403(e):
    return render_template("error_pages/403.html"), 403
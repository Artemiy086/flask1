from flask  import render_template, Blueprint, url_for


bp_users = Blueprint("users", __name__, url_prefix='')


@bp_users.route("/")
def index():
    return render_template("index.html")


@bp_users.route("/image_mars_last")
def image_mars_last():
    return render_template("image_mars_last.html")


@bp_users.route("/image_mars")
def image_mars():
    return render_template("image_mars.html")

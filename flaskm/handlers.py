import os

from flask import render_template, Blueprint, url_for, request, flash, redirect, current_app
from werkzeug.utils import secure_filename

bp_users = Blueprint("users", __name__, url_prefix='')


def save_file(request):
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('download_file', name=filename))


@bp_users.route("/")
def index():
    return render_template("index.html", title="главная")


@bp_users.route("/image_mars_last")
def image_mars_last():
    return render_template("image_mars_last.html", title="image_mars_last")


@bp_users.route("/promotion_image")
def image_mars():
    return render_template("promotion_image.html", title="promotion_image")


@bp_users.route("/astronaut_selection", methods=["GET", "POST"])
def astronaut_selection():
    select_option = ["Начальной", "Среднее", "Высшее"]
    professions = ["пилот", "Врач", "Инженер", "Метеоролог", "Строитель"]

    if request.method == "GET":
        return render_template("astronaut_selection.html", title="astronaut_selection",
                               select_option=select_option, professions=professions, enumerate=enumerate)
    print(request.form.get("name"), 1)
    return redirect("/")

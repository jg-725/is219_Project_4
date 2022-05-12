import csv
import json
import logging
import os

from flask import Blueprint, render_template, abort, url_for, current_app, jsonify, flash
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from werkzeug.utils import secure_filename, redirect
from flask import Response

csv_files_upload = Blueprint('csv_files_upload', __name__,
                        template_folder='templates')



@csv_files_upload.route('/upload', methods=['POST', 'GET'])
@login_required
def file_upload():
    form = csv_upload()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            header = next(csv_file)
            print(header)
            rows = []
            for row in csv_file:
                rows.append(row)
                if row is None:
                    db.session.commit()
                else:
                    current_user.rows.append(row)
                    db.session.commit()
        return redirect(url_for('csv_files_upload.browse_locations'))

    try:
        return render_template('upload_locations.html', form=form)
    except TemplateNotFound:
        abort(404)
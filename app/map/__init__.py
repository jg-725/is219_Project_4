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

map = Blueprint('map', __name__,
                        template_folder='templates')



@map.route('/locations/upload', methods=['POST', 'GET'])
@login_required
def location_upload():
    form = csv_upload()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        list_of_locations = []
        with open(filepath) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                location = Location.query.filter_by(title=row['location']).first()
                if location is None:
                    current_user.locations.append(Location(row['location'],row['longitude'],row['latitude'],row['population']))
                    db.session.commit()
                else:
                    current_user.locations.append(location)
                    db.session.commit()
        return redirect(url_for('map.browse_locations'))

    try:
        return render_template('upload_locations.html', form=form)
    except TemplateNotFound:
        abort(404)
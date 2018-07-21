#coding:utf-8
from flask import jsonify, request, Response
from . import api
from app import db
from app.models import User, PGoal 
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.sql import func
import random
import json

@api.route('/questionnaire/application/<int:uid>/', methods = ['POST'])
def apply(uid):
    if request.method == 'POST':
        token = request.headers['token']
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            sgoal = request.get_json().get('sgoal')
            for x in sgoal:
                pgoal = PGoal(name = x.get('name'),
                        hour = x.get('hour'),
                        ddl = x.get('ddl'),
                        result = 0,
                        PorS = 1,
                        importance = x.get('importance'),
                        user_id = uid)
                db.session.add(pgoal)
                db.session.commit()
            return 200




                




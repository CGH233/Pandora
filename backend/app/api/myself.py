#coding:utf-8
from flask import jsonify, request, Response
from . import api
from app import db
from app.models import User, PGoal
from flask_login import login_user, logout_user, current_user, login_required
import json
import time

@api.route('/user/<int:uid>/detal/', methods = ['GET'])
def detal(uid):
    if request.method == 'GET':
        token = request.headers['token']
        print(uid)
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            pgoal = PGoal.query.filter_by(user_id=uid)
            goal = []
            sn = 0
            sf = 0
            pn = 0
            pf = 0
            for x in pgoal:
                pgoal1 = PGoal.query.filter_by(id=x.id).first()
                goal.append({"importance":pgoal1.importance,
                             "name":pgoal1.name,
                             "hour":pgoal1.hour,
                             "ddl":pgoal1.ddl,
                             "result":pgoal1.result,
                             "gid":pgoal1.id})
                if (pgoal1.PorS == 1):
                    sn += 1
                    if (pgoal1.result == 1):
                        sf += 1
                else:
                    pn += 1
                    if (pgoal1.result == 1):
                        pf += 1
            if (sn == 0):
                a = 0
            else:
                a = sf / sn
            if (pn == 0):
                b = 0
            else:
                b = pf / pn
            return jsonify({"username":user.username,
                            "score":user.score,
                            "sstatus":a,
                            "pstatus":b,
                            "time":time.strftime("%Y-%M-%D",time.localtime()),
                            "goal":goal
                            }),200

@api.route('/user/<int:uid>/<int:gid>/result/', methods = ['POST'])
def result(uid,gid):
    if request.method == 'POST':
        token = request.headers['token']
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            result = request.get_json().get('result')
            goal = PGoal.query.filter_by(id=gid).first()
            goal.result = result
            db.session.add(goal)
            db.session.commit()
            return jsonify(),200    

@api.route('/user/<int:uid>/addition/', methods = ['POST'])
def additoin(uid):
    if request.method == 'POST':
        token = request.headers['token']
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            importance = request.get_json().get('importance')
            name = request.get_json().get('name')
            hour = request.get_json().get('hour')
            ddl = request.get_json().get('ddl')
            goal = PGoal(name = name,
                         hour = hour,
                         ddl = ddl,
                         importance = importance,
                         result = 0,
                         PorS = 0,
                         user_id = uid)
            db.session.add(goal)
            db.session.commit()
            return jsonify({"gid":goal.id}),200

@api.route('/user/<int:uid>/<int:gid>/exchange/', methods = ['POST'])
def exchange(uid,gid):
    if request.method == 'POST':
        token = request.headers['token']
        user = User.query.filter_by(id=uid).first()
        if user.confirm(token):
            importance = request.get_json().get('importance')
            name = request.get_json().get('name')
            hour = request.get_json().get('hour')
            ddl = request.get_json().get('ddl')
            cost = request.get_json().get('cost')
            goal = PGoal.query.filter_by(user_id=user.id).first()
            goal.name = name
            goal.hour = hour
            goal.ddl = ddl
            goal.importance = importance
            goal.result = 0
            goal.PorS = 0
            if int(user.score) >= int(cost):
                user.score = int(user.score) - int(cost)
                db.session.add(goal,user)
                db.session.commit()
                return jsonify({"message":"1"}),200
            else:
                return jsonify({"message":"0"}),400


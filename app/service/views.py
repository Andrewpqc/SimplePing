from flask import jsonify,Response
from . import service
from app.models import Requirement,PingInfo
from manage import command_360,command_vivo,command_baidu
from app import db
import json

@service.route('/simpleping')
def index():
    a=[]
    pinginfos=PingInfo.query.all()
    for pinginfo in pinginfos:
        temp={}
        temp["company"]=pinginfo.company
        temp["category"]=pinginfo.category
        temp["pingType"]=pinginfo.pingType
        temp["jobTitle"]=pinginfo.jobTitle
        temp["time"]=pinginfo.time
        temp["location"]=pinginfo.location
        temp["link"]=pinginfo.link
        temp["email"]=pinginfo.email
        temp["requirements"]=[]
        for req in pinginfo.requirements:
            temp["requirements"].append(req.text)
        a.append(temp)
    return Response(json.dumps(a),mimetype="application/json")

@service.route("/flush")
def flush():
    try:
        db.drop_all()
        db.create_all()
        command_baidu()
        command_360()
        command_vivo()
    except Exception as e:
        print(e)
        return "ERROR"
    else:
        return "OK"







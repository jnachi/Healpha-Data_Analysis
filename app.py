from flask import Flask, render_template, request, jsonify
from process import process
from expand import expand
from expand import pop
from excel_process import print
from flask_cors import CORS,cross_origin
from json import dumps

app =Flask(__name__)
CORS(app, support_credentials=True)
cross_origin(support_credentials=True)#for using files from internet

@app.route('/test', methods=["POST"])
def index():
    y=process()
    return dumps([y])
@app.route('/test2', methods=["POST"]) #populating the drop down list after change in branch id in dig
def second():
    data = request.get_json()
    y=pop(data['data'])
    return dumps([y])
@app.route('/test1', methods=["POST"]) #sending parameter from dig
def first():
    data = request.get_json()
    print(data)
    y=expand(data['data'][0],data['data'][1],data['data'][2],data['data'][3])
    return dumps([y])

@app.route('/excel', methods=["POST"])
def third():
    name= request.get_json()
    y = print(name)
    return jsonify([y])




if __name__ =='__main__':
    app.run()
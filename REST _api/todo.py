from flask import Flask,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

todo={}
class todo_method(Resource):
    def get(self,todo_id):
        return {"todo_ex":todo[todo_id]}
    def put(self,todo_id):
        todo[todo_id]=request.form["data"]
        return {"todo_ex":todo[todo_id]}
    def post(self,todo_id):
        todo[todo_id]=request.form["data"]
        return{"todo_ex":todo[todo_id]}
    def patch(self,todo_id):
        todo[todo_id]=request.form["data"]
        return{"todo_ex":todo[todo_id]}
    def delete(self,todo_id):
        todo[todo_id]=request.form["data"]
        return{"todo_ex":todo[todo_id]}

    
    

api.add_resource(todo_method,"/<string:todo_id>")         #Helloworld is class name



if __name__=="__main__":
    app.run(debug=True,port=5001)

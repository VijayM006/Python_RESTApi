from flask import Flask
from flask_restful import Resource,Api
vj=Flask(__name__)
api=Api(vj)


class Helloworld(Resource):
    def get(self):
        return {"Message":"Vijay","Loves":"Maris"}
    
api.add_resource(Helloworld,"/a")         #Helloworld is class name



if __name__=="__main__":
    vj.run(debug=True,port=5002)
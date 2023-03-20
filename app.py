from flask import Flask ,render_template,request,url_for
from pymongo import MongoClient
app=Flask(__name__)

#client =MongoClient("mongodb+srv://deepak:Deepak123@krushi-mitra.pczs8cq.mongodb.net/test")

#db=client.KrushiMitra


 
entries = []

 
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/register_main',methods =['GET',"POST"])
# def about():
# #     if request.method=='POST':
# #         name=request.form.get('Name')
# #         Email =request.form.get('Email')
# #         Password =request.form.get('password')
# #         db.Regester.insert_one({"User_Name":name,'User_Email':Email,"User_Password":Password})
# #         print(Password)
   
# #     print('Hello')
# #     print(db.list_collection_names())
# #     print([e for e in db.Regester.find({})])
#     return render_template('register_main.html')

# @app.route('/register_main')
# def home():
#     return render_template('register_main.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
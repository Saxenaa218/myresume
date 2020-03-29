from flask import Flask,render_template,request
app = Flask(__name__)
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["tests"]
# mycol = mydb["all_data"]

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3039,debug = True)

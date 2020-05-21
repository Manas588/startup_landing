from flask import Flask, render_template,jsonify, request
# from flask_cors import CORS,cross_origin
import json
import csv
app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = False


@app.route('/<string:route>')
def route(route):
   return render_template(f'{route}')

@app.route('/form_submitted', methods=["POST"])
def form():
   with open('database.csv', 'a', newline='') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow([request.form["email"], request.form["name"], request.form["subject"], request.form["message"]])
    

   if request.form["name"]:
      hello =request.form["name"]
   else:
      hello =request.form["email"]
   
   return render_template('form_submitted.html', name=hello)


@app.route('/messages')
def messages():
   with open('database.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
      ob = {}
      i = 0
      for row in spamreader:
         ob[str(i)] = {"name": row[1],
                       "email": row[0],
                       "subject": row[2],
                       "message": row[3]
                        }
         i += 1
      return jsonify(ob)



if __name__ == "__main__":
    app.run()
    
   
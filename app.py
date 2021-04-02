import flask
from flask import request, jsonify
from flask_cors import cors
from random import randrange
import json
import random

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

with open("cat-facts.json") as json_file:
  cat_data = json.load(json_file)
  cat_data_length = len(cat_data)

with open("dog-facts.json") as json_file:
  dog_data = json.load(json_file)
  dog_data_length = len(dog_data)

@app.route('/')
def home():
  return "<h1>Cat (and Dog) Facts API</h1>"

@app.errorhandler(404)
def page_not_found(e):
  return "<h1>Error 404:</1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/facts', methods=['GET'])
def api_number():
  results = {}
  
  data = cat_data
  data_length = cat_data_length
  if 'animal_type' in request.args:
    animal_type = request.args['animal_type']
    if animal_type == 'dog':
      data = dog_data
      data_length = dog_data_length
    elif animal_type == 'cat':
      data = cat_data
      data_length = cat_data_length
    else: 
      return page_not_found(404)

  if 'id' in request.args:
    index = int(request.args['id'])
    if index >= 0 and index < data_length:
      results['text'] = data[index]
      results['id'] = index
  else:
    index = random.randint(0, data_length - 1)
    results['text'] = data[index]
    results['id'] = index
      
  return jsonify(results)

if __name__ == '__main__':
  app.run()
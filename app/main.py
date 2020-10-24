from flask import Flask
from flask import jsonify
import json
from Transform import Transform

app = Flask("flask")

transform = Transform()

@app.route("/")
def route():
  return {"villeChoisie":"Montreal"}

@app.route('/extracted_data')
def show_extracted_data():
  nbRestaurants = transform.get_nbRestaurants()
  nbSegments = transform.get_nbSegments()

  extracted_data = {}
  extracted_data['nbRestaurants'] = nbRestaurants['nbRestaurants']
  extracted_data['nbSegments'] = nbSegments

  return extracted_data
  

@app.route('/transformed_data')
def show_transformed_data():
  nbRestaurants_type = transform.get_nbRestaurants_type()
  longueurCyclable = transform.get_longueurCyclable()

  transformed_data = {}
  transformed_data['restaurants'] = nbRestaurants_type['restaurants']
  transformed_data['longueurCyclable'] = longueurCyclable

  return transformed_data
  
if __name__ == "__main__":
  app.run('0.0.0.0', port=80, debug=True)
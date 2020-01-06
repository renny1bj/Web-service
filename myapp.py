from flask import Flask , jsonify, render_template
from requests import get
import json

myapp = Flask(__name__)

@myapp.route("/animal_database",methods=["GET"])
def fect_my_data():
    res = get('http://localhost:9200/animal/_search?size=300')
    data = res.json()
    return jsonify(data)

@myapp.route("/accueil",methods=["GET"])
def get_home_page():
    return render_template('accueil.html')



#road to Animal
@myapp.route("/animals_database",methods=["GET"])
def get_animal():
    res = get('http://localhost:9200/animal/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('animals_database.html',database=database)




#road to hobbies and sport
@myapp.route("/sport_hobbies",methods=["GET"])
def get_sport_hobbies():
    res = get('http://localhost:9200/hobbies/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('sport_Hobbies.html',database=database)


#road to vehicule
@myapp.route("/vechile_database",methods=["GET"])
def get_vechile():
    res = get('http://localhost:9200/vehicule/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('vechile_database.html',database=database)



#road to appliances
@myapp.route("/electronic_database",methods=["GET"])
def get_electronic():
    res = get('http://localhost:9200/electronique/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('electronic_database.html',database=database)




#road to computer
@myapp.route("/computer_databases",methods=["GET"])
def get_computer():
    res = get('http://localhost:9200/computer/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('computer_databases.html',database=database)



# road to agroaliment-groupe 5
@myapp.route("/agroaliment",methods=["GET"])
def get_agroaliment():
    res = get('http://localhost:9200/agroaliment/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('agroaliment.html',database=database)


#road to base
@myapp.route("/base",methods=["GET"])
def get_base():
    res = get('http://localhost:9200/base/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('base.html',database=database)


#road to emploie
@myapp.route("/emploie",methods=["GET"])
def get_emploie():
    res = get('http://localhost:9200/emploie/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('emploie.html',database=database)




#road to house
@myapp.route("/house",methods=["GET"])
def get_house():
    res = get('http://localhost:9200/house/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('house.html',database=database)



#road to terrain_database
@myapp.route("/terrain_database",methods=["GET"])
def get_terrain_database():
    res = get('http://localhost:9200/terrain_database/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('terrain_database.html',database=database)



#road to equipement_maison


#road to electrique
@myapp.route("/car_database",methods=["GET"])
def get_electronique():
    res = get('http://localhost:9200/group_1_database/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('electronique.html',database=database)




#road to eletromenager
@myapp.route("/electromenager",methods=["GET"])
def get_electromenager():
    res = get('http://localhost:9200/electromenager_database/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('electromenager.html',database=database)



# mode
@myapp.route("/modedataGroup7", methods=["GET"])
def view_modedata():
    res = get("http://localhost:9200/modedata/_search?size=300")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("modedataGroup7.html", database=database)



@myapp.route("/phone", methods=["GET"])
def get_phone():
    res = get("http://localhost:9200/phone/_search?size=300")
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template("phone.html", database=database)


@myapp.route("/equipement_maison",methods=["GET"])
def get_equipement_maison():
    res = get('http://localhost:9200/equipement_maison/_search?size=300')
    data = json.loads(res.text)
    database = data['hits']['hits']
    return render_template('equipement_maison.html',database=database)



@myapp.route("/database_list",methods=["GET"])
def list_database():
    return render_template('list_database.html')

if __name__ == '__main__':
    myapp.run(debug=True)
    #app.run(host='localhost', port=9874)

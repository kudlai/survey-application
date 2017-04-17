from flask import Flask
from flask import Response
import yaml
import json
import MySQLdb

app = Flask(__name__)
cfg = None
with open("/webapp/config.yaml") as conf_file:
    cfg = yaml.load(conf_file)
        


@app.route("/")
def main_route():
    query = "select first_name, last_name from employees where birth_date = '1965-02-01' and hire_date > '1990-01-01' and gender = 'M' order by first_name, last_name;"
    con = MySQLdb.connect(passwd=cfg['mysql']['password'], user=cfg['mysql']['user'], host=cfg['mysql']['host'], port=cfg['mysql']['port'], db="employees")
    cur = con.cursor()
    cur.execute(query)
    results = []
    for row in cur.fetchall():
        first_name, last_name = row
        results.append("%s %s" % (first_name, last_name))
    return Response(json.dumps(results), mimetype='text/json') 
 

@app.route("/full")
def full_route():
    query = "select emp_no, birth_date, first_name, last_name, gender, hire_date from employees where birth_date = '1965-02-01' and hire_date > '1990-01-01' and gender = 'M' order by first_name, last_name;"
    con = MySQLdb.connect(passwd=cfg['mysql']['password'], user=cfg['mysql']['user'], host=cfg['mysql']['host'], port=cfg['mysql']['port'], db="employees")
    cur = con.cursor()
    cur.execute(query)
    results = []
    for row in cur.fetchall():
        emp_no, birth_date, first_name, last_name, gender, hire_date = row
        birth_date_str = birth_date.strftime("%Y-%m-%d")
        hire_date_str = hire_date.strftime("%Y-%m-%d")
        results.append({'emp_no': emp_no, 'birth_date': birth_date_str, 'first_name': first_name, 'last_name': last_name, 'gender': gender, 'hire_date': hire_date_str})
    return Response(json.dumps(results), mimetype='text/json') 
 
if __name__ == "__main__":
    app.run()

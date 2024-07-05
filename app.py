from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Faisalabad, Pakistan',
        'salary': 'Rs. 200,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs. 300,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 150,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$80,000'
    },
    {
        'id': 5,
        'title': 'Full Stack Engineer',
        'location': 'London, UK',
        'salary': '$100,000'
    }
]


@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS, company_name='Quantum')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

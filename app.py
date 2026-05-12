from flask import Flask, render_template

app = Flask(__name__)

# Dummy Data: Ye hamara temporary database hai
leads_data = [
    {"id": 1, "name": "Ali Khan", "email": "ali@example.com", "status": "New"},
    {"id": 2, "name": "Sara Ahmed", "email": "sara@example.com", "status": "Contacted"},
    {"id": 3, "name": "Bilal Tariq", "email": "bilal@example.com", "status": "Converted"}
]

@app.route('/')
def dashboard():
    # Yahan hum leads_data ko 'leads' variable ke naam se HTML file me bhej rahe hain
    return render_template('index.html', leads=leads_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
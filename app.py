from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    # In a real scenario, you'd send an email here using Flask-Mail
    print(f"New Inquiry from {data['name']}: {data['message']}")
    return jsonify({"status": "success", "msg": "Message received! I'll contact you soon."})

if __name__ == '__main__':
    app.run(debug=True)
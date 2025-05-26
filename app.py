from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    message = data.get("message")


    if message == "Get instagram-target link":
        return jsonify({"response": "Get instagram-target link Link: https://t.me/c/2344120391/214/233"})
    elif message == "Get instagram-target":
        return jsonify({"response": "Get instagram-target1 link Link: https://t.me/c/2267427894/620"})
    else:
        return jsonify({"response": "❌ Invalid request. Please try again."})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

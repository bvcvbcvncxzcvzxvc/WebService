from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    message = data.get("message")

    if message == "Get EagleSpy-V5 link":
        return jsonify({"response": "Get EagleSpy-V5 link Link: https://t.me/c/2344120391/214/233"})
    elif message == "Get CraxsRat-7.6 link":
        return jsonify({"response": "Get CraxsRat-7.6 link Link: https://t.me/c/2267427894/620"})
    else:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

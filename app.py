from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Simple Chat Agent is running! Use /chat?message=hello to talk."

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        message = request.args.get('message', '')
    else:
        data = request.get_json()
        message = data.get('message', '') if data else ''
    
    if not message:
        return jsonify({"response": "I didn't hear anything. What's on your mind?"})
    
    # Simple logic for now. 
    # In a real scenario, you'd connect to an LLM API here.
    response = f"You said: {message}. I'm a simple agent hosted on Render!"
    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
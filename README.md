# Simple Chat Agent

A simple Flask-based chat agent that can be hosted on Render.

## Deployment to Render

1. Create a new "Web Service" on Render.
2. Connect this GitHub repository.
3. Render will automatically detect the 'Procfile' and 'requirements.txt'.
4. Once deployed, you can talk to the agent via the provided URL.

## API Usage

- **Endpoint**: /chat
- **Method**: GET or POST
- **Parameter**: message
- **Response**: JSON {"response": "..."}
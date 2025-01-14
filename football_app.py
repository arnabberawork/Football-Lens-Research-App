from flask import Flask, request, jsonify
from football_agent import run_crew_ai_football
import logging

# Configure logging to file
logging.basicConfig(filename="app_errors.log", level=logging.ERROR)

app = Flask(__name__)

@app.route("/generate_blog", methods=["POST"])
def generate_blog():
    # Get input from the request
    data = request.get_json()
    topic = data.get('topic', 'Football')
    sector= data.get('sector', 'Sports')
    creativity_limit = data.get('creativity_limit', 0.5)
    # Here you will call the previously provided code to generate the blog post
    try:
        # You can customize the behavior of creativity limit in your agent and writing process
        result = run_crew_ai_football(topic, sector, creativity_limit)  # Replace with the real function
        logging.info(f"Generated blog result: {result.raw}")  # Log the result to check its structure
        return jsonify({"status": "success", "message": "Blog generated successfully!", "blog_post": result.raw}), 200
    
    except Exception as e:
        logging.error(f"Error generating blog: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Replace with your DeepAI API key
DEEP_AI_API_KEY = "5faa26dc-a9c6-4b8d-9b2d-eb7dac71a852"

@app.route('/')
def home():
    # Render the HTML frontend
    return render_template("index.html")

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Send request to DeepAI API
    try:
        response = requests.post(
            "https://api.deepai.org/api/text2img",
            data={'text': prompt},
            headers={'api-key': DEEP_AI_API_KEY}
        )
        result = response.json()
        if 'output_url' in result:
            return jsonify({"image_url": result['output_url']})
        return jsonify({"error": result.get('err', 'Image generation failed')}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-video', methods=['POST'])
def generate_video():
        data = request.json
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Send request to DeepAI API
        try:
            response = requests.post(
                "https://api.deepai.org/api/video-generator",
                data={'text': prompt},
                headers={'api-key': DEEP_AI_API_KEY}
            )
            result = response.json()
            if 'output_url' in result:
                return jsonify({"video_url": result['output_url']})
            return jsonify({"error": result.get('err', 'video generation failed')}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

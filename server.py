import os
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['POST'])
def get_transcript():
    try:
        video_id = request.json.get('video_id')
        if not video_id:
            return jsonify({'error': 'Video ID is required'}), 400

        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcript), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Use the PORT environment variable provided by Render
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)

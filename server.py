from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['POST'])
def get_transcript():
    try:
        # Get the video ID from the request
        video_id = request.json.get('video_id')
        if not video_id:
            return jsonify({'error': 'Video ID is required'}), 400

        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify(transcript), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)

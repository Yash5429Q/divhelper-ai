"""
Main API Module
Handles core API endpoints and request routing
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/process', methods=['POST'])
def process_request():
    """Process incoming requests"""
    try:
        data = request.get_json()
        # Process request logic here
        return jsonify({'success': True, 'message': 'Request processed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

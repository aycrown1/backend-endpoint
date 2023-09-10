from flask import Flask, request, jsonify, abort
from datetime import datetime

endpoint = Flask(__name__)

@endpoint.route('/api', methods=['GET'])
def get_api_data():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    current_day = datetime.now().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = "https://github.com/aycrown1/backend-endpoint/blob/main/endpoint.py"
    github_repo_url = "https://github.com/aycrown1/backend-endpoint"
    status_code = "200"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    response =  jsonify(response_data)

    return response

if __name__ == '__main__':
    endpoint.run(debug=True)

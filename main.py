from flask import Flask, make_response, request
from db import get_authors_from_database
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main(request):
    """Scrape scheduled link previews.

    1. Set headers of fetch request.
    2. Call get_meta constructor.
    3. Convert metadata to JSON object.
    4. Return response.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)
    if request.method == 'GET':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        author_slug = request.args['author']
        author = get_authors_from_database(author_slug)
        return make_response(str(author), 200, headers)


if __name__ == '__main__':
    app.run(debug=True)

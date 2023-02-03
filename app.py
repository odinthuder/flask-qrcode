from flask import Flask, request, Response
from qrcode import make

app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr():
    url = request.args.get('url')
    if not url:
        return 'Error: No URL provided.', 400
    img = make(url)
    return Response(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
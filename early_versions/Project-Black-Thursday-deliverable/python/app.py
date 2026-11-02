"""Offline-first local server. Uses Flask when installed; stdlib fallback works without pip.

Run from project root: python python/app.py
"""
from pathlib import Path
import json
import mimetypes
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from simulation import MODEL_VERSION, simulate

try:
    from flask import Flask, request, jsonify, send_from_directory
except ImportError:
    Flask = None

if Flask is not None:
    app = Flask(__name__, static_folder=None)
    @app.get('/api/health')
    def health(): return jsonify({'status':'ok','model_version':MODEL_VERSION})
    @app.post('/api/simulate')
    def api_simulate():
        try: return jsonify(simulate(request.get_json(silent=True)))
        except (ValueError, TypeError) as error: return jsonify({'error':str(error)}),400
    @app.get('/')
    def index(): return send_from_directory(ROOT / 'presentation', 'index.html')
    @app.get('/<path:filename>')
    def assets(filename):
        # Resolves only a small list of intentional public roots.
        if filename.startswith(('presentation/','media/','animation/')):
            return send_from_directory(ROOT, filename)
        return 'Not found',404
else:
    app = None

class StandardLibraryApp:
    """WSGI-compatible zero-dependency fallback, same routes and API."""
    def __call__(self, environ, start_response):
        method, path = environ.get('REQUEST_METHOD','GET'),environ.get('PATH_INFO','/')
        if path == '/api/health' and method == 'GET':
            status,ct,body='200 OK','application/json',json.dumps({'status':'ok','model_version':MODEL_VERSION}).encode()
        elif path == '/api/simulate' and method == 'POST':
            try:
                length=int(environ.get('CONTENT_LENGTH','0') or '0')
                if length > 16384: raise ValueError('הבקשה גדולה מדי.')
                payload=json.loads(environ['wsgi.input'].read(length))
                result=simulate(payload)
                status='200 OK'
            except (ValueError,TypeError,KeyError,json.JSONDecodeError) as error:
                result={'error':str(error)}
                status='400 Bad Request'
            ct,body='application/json',json.dumps(result,ensure_ascii=False).encode('utf-8')
        elif method == 'GET' and (path == '/' or path.startswith(('/presentation/','/media/','/animation/'))):
            relative='presentation/index.html' if path=='/' else path.lstrip('/')
            file=(ROOT / relative).resolve()
            if not file.is_relative_to(ROOT) or not file.is_file():
                status,ct,body='404 Not Found','text/plain',b'Not found'
            else:
                status='200 OK'; ct=mimetypes.guess_type(str(file))[0] or 'application/octet-stream';body=file.read_bytes()
        else: status,ct,body='404 Not Found','text/plain',b'Not found'
        start_response(status,[('Content-Type',ct+'; charset=utf-8' if ct.startswith(('text/','application/json')) else ct),('Content-Length',str(len(body))),('Cache-Control','no-store')])
        return [body]

def run():
    if Flask is not None:
        print('Running Flask at http://127.0.0.1:8000/')
        app.run(host='127.0.0.1',port=8000,debug=False)
    else:
        from wsgiref.simple_server import make_server
        print('Flask not installed. Running compatible Python stdlib server at http://127.0.0.1:8000/',flush=True)
        with make_server('127.0.0.1',8000,StandardLibraryApp()) as srv:
            srv.serve_forever()

if __name__=='__main__':run()

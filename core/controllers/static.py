from bottle import request, static_file
from core import app, static_path

@app.get('/')
def app_index():
    """Render home page"""
    return static_file('app.index.html', root=static_path)

@app.route('/assets/<file:path>', method='GET')
def get_assets(file):
    """Returns files from static assets directory"""
    return static_file(file, root='{}/assets/'.format(static_path))

@app.route('/app/<file:path>', method='GET')
def get_app(file):
    """Returns files from static app directory"""
    return static_file(file, root='{}/static/app/'.format(base_path))
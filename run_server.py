from aiobottle import AsyncBottle
import aiohttp
from bottle import jinja2_view, request

# Initialize aiobottle app
app = AsyncBottle()

@app.get('/')
@jinja2_view('home.html', template_lookup=['views'])
def home():
    """Render home page"""
    return {'env': str(request.environ)}

def main(host='::', port=8080):
    """Start Bottle server"""
    from bottle import run
    run(app, host = host, port = port, server = 'aiobottle:AsyncServer')

if __name__ == '__main__':
    main()
import os
import sys

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
# Add working directory to paths
sys.path.append(os.path.dirname(__file__))

from core import app
from core.controllers import *

def main(host='::', port=8080):
    """Start Bottle server"""
    from bottle import run
    run(app, host = host, port = port, server = 'aiobottle:AsyncServer')

if __name__ == '__main__':
    main()
from aiobottle import AsyncBottle
import os

core_path = os.path.dirname(os.path.abspath(__file__))
static_path = '{}/static'.format(core_path)

from tornroutes import route

from core.controllers import *

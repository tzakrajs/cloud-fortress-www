from aiobottle import AsyncBottle
import logging
import os

# config log format
format="%(asctime)-21s %(levelname)s %(name)s (%(funcName)-s) " + \
       "%(process)d:%(thread)d - %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=format,
                    filename='./cloud-fortress-www.log')

from tornroutes import route

from core.controllers import *

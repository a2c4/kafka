from __future__ import division
## event lib
from gevent import monkey;monkey.patch_all()
from gevent.pywsgi import WSGIServer
## mqtt libraries
import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTv311
## kafka client lib
from pykafka import KafkaClient
from pykafka.common import OffsetType
## dt lib
import time
from datetime import datetime
## pseudo random lib
from random import randrange, uniform
import random
from geopy.geocoders import Nominatim
from faker import Faker
## Jsonify lib
import json
## math lib
import math
## iter lib
from itertools import islice
## flask lib
from flask import Flask, render_template, Response
from flask import Flask, Response, render_template, stream_with_context
import sqlite3

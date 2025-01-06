from flask import Flask, request, jsonify
import openstack

app = Flask(__name__)

conn = openstack.connect(
    
)
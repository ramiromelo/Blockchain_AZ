# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:39:23 2021

@author: RAMIRO
"""


import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
        
# Part 2 - Mining a Blockchain

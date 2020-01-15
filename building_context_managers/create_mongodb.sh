#!/bin/bash

# Install as:
# sudo apt install mongodb
# pip install pymongo

# Create local db and run server:
mongod --dbpath data/

# Test connection to db via CLI:
# mongo
# use test
# db.collection.insert_one({'item': "card", 'qty': 15})
# db.collecton.find()

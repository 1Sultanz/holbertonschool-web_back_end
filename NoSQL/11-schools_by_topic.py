#!/usr/bin/env python3
"""Where can I learn Python?"""

def schools_by_topic(mongo_collection, topic):
    """return specific from a MongoDB collection"""
    result =  mongo_collection.find_one({"topic": topic})
    return result

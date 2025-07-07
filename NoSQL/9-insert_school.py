#!/usr/bin/env python3
"""Insert a document in a Python"""

def insert_school(mongo_collection, **kwargs):
    """Insert a document to a MongoDB collection"""
    doc = list(mongo_collection.insert(**kwargs)
               return doc

#!/usr/bin/env python3
"""Change school topics"""

 def update_topics(mongo_collection, name, topics):
     """Update topics of school"""
     doc = mongo_collection.update_one(name, topics)
     return doc

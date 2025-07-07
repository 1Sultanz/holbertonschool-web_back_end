#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """Lists all documents in a collection"""
    documents = list(mongo_collection.find())
    return documents

import os
from app import app
from flask import request, render_template, jsonify, json
from pdfrw import PdfReader, PdfWriter, PageMerge

@app.route('/')
def index():
    ipdf = PdfReader('book.pdf')
    return str(len(ipdf.pages))
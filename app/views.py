import os
from app import app
from flask import request, render_template, jsonify, json, send_file
from pdfrw import PdfReader, PdfWriter, PageMerge

@app.route('/')
def index():
    ipdf = PdfReader('book.pdf')
    return str(len(ipdf.pages))

@app.route('/test')
def test_send():
    return send_file('book.pdf')

@app.route('/cut_pdf/<int:start>/<int:end>')
def test_cut(start, end):
    ipdf = PdfReader('../pdfs/book.pdf')
    opdf = PdfWriter()
    for i in range(start, end):
        opdf.addpage(ipdf.pages[i])
    opdf.write('pdfs/result.pdf')

    ipdf = PdfReader('../pdfs/result.pdf')

    return send_file('../pdfs/result.pdf')
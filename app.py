from flask import Flask, render_template, flash, redirect, request, json
import os
import urllib.request
from jinja2 import ext
from datetime import datetime

app = Flask(__name__)



def format_time2(gig):
    return datetime.strptime(gig, '%Y-%m-%dT%H:%H:%M:%M:%S.%f').strftime('%d. %m. %Y kl. &H %M')


# bensínstöðvar
with urllib.request.urlopen("https://apis.is/petrol") as url:
    gogn = json.loads(url.read().decode())


def format_time(gogn):
    return datetime.strptime(gogn, '%Y-%m-%dT%H:%H:%M:%M:%S.%f').strftime('%d. %m. %Y kl. &H %M')


app.jinja_env.add_extension(ext.do)

app.jinja_env.filters['format_time'] = format_time
app.jinja_env.filters['format_time'] = format_time2

"""lægsta verðið"""


def minPetrol():
    minPetrolPrice = 1000
    company = None
    address = None
    lst = gogn['results']
    for i in lst:
        if i['bensin95'] is not None:
            if i['bensin95'] < minPetrolPrice:
                minPetrolPrice = i['bensin95']
                company = i['company']
                address = i['name']
    return [minPetrolPrice, company, address]


def minDisel():
    minDiselPrice = 1000
    company = None
    address = None
    lst = gogn['results']
    for i in lst:  # loopum í gegnum allt datasettið
        if i['bensin95'] is not None:  # hreinsum burt öll tilvik af "null"
            if i['bensin95'] < minDiselPrice:
                minDiselPrice = i['bensin95']
                company = i['company']
                address = i['name']
    return [minDiselPrice, company, address]  # skila lista af lægsta verði, nafn fyrirtækis og heimilisfang


@app.route('/')
def index():
    return render_template('index.tpl', gogn=gogn, minP=minPetrol(), minD=minDisel())


@app.route('/company/<company>')
def comp(company):
    return render_template('company.tpl', gogn=gogn, com=company)


@app.route('/moreinfo/<key>')
def info(key):
    return render_template('moreinfo.tpl', gogn=gogn, k=key)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.tpl'), 404


if __name__ == '__main__':
    app.run(debug=True)
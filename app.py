from flask import Flask
from flask import render_template
from appium import webdriver
import time
from cases.rydezillaUserIosQa import browserStackCaller as rydezillaUserIosQA

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

userName = "khalednakawa_9RsPlD"
accessKey = "9qktLEF5WzzPx3xwp5VN"

@app.route("/")
def hello_world():
    print("testt")
    return render_template("index.html")

@app.route("/trigger")
def trigger():
    return rydezillaUserIosQA(webdriver,time,userName,accessKey)



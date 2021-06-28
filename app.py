from flask import Flask
from flask import render_template
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("testt")
    return render_template("index.html")

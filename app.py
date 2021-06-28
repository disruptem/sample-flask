from flask import Flask
from flask import render_template
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)


userName = "khalednakawa_jskeyQ"
accessKey = "gq16w425AZqW3SA5nPM2"

desired_caps = {
    "build": "browser_sample2",
    "name" : "test 15",
    "device": "iPhone 12 Pro",
    "os_version" : "14",
    "app": "bs://ac09441d0ad0f46bc4daa57af4553806ea6b8526",
    # "browserstack.appium_version" : "1.21.0",
    # "browserstack.acceptInsecureCerts" : "true",
    # 'autoDissmissAlerts': 'true',
     "autoAcceptAlerts" : "true",
    # "autoGrantPermissions": "true",
    # "gpsEnabled" : "true",
}


@app.route("/")
def hello_world():
    print("testt")
    return render_template("index.html")

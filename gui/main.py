import os
import dateutil.parser
from flask import Flask, render_template, redirect
from antihate.settings.settings import get_parm, set_parm, json
from antihate.app import App as systemApp


def take_json(number=None):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "../antihate", "stats_file.json")
    data = json.load(open(json_url))
    data = data['stats']
    fromDate, toDate, offensiveData, hateData = cutData(data, number)
    return fromDate, toDate, offensiveData, hateData


def cutData(data, number=None):
    fromDate = []
    toDate = []
    offensiveData = []
    hateData = []
    start_step = int(number) * 10
    end_step = (int(number) + 1) * 10
    if start_step > len(data):
        for i in data:
            fromDate.append(dateutil.parser.parse(i['from_date']).timestamp())
            toDate.append(dateutil.parser.parse(i['to_date']).timestamp())
            offensiveData.append(i['offensive_language'])
            hateData.append(i['hate_speech'])
    else:
        if end_step > len(data):
            for i in range(start_step, len(data)):
                fromDate.append(dateutil.parser.parse(data[i]['from_date']).timestamp())
                toDate.append(dateutil.parser.parse(data[i]['to_date']).timestamp())
                offensiveData.append(data[i]['offensive_language'])
                hateData.append(data[i]['hate_speech'])
        else:
            for i in range(start_step, end_step):
                fromDate.append(dateutil.parser.parse(data[i]['from_date']).timestamp())
                toDate.append(dateutil.parser.parse(data[i]['to_date']).timestamp())
                offensiveData.append(data[i]['offensive_language'])
                hateData.append(data[i]['hate_speech'])
    return fromDate, toDate, offensiveData, hateData


sApp = systemApp.instance()
sApp.start()
app = Flask(__name__)


@app.route(
    '/settings/save/<user_email>/<collect_interval>/<analysis_interval>/<limit_hate_ratio>/<limit_hate_sum>/<list_len>')
def saveSettings(user_email=None, collect_interval=None, analysis_interval=None,
                 limit_hate_ratio=None, limit_hate_sum=None, list_len=None):
    set_parm("user_email", user_email)
    set_parm("collect_interval", int(collect_interval))
    set_parm("analysis_interval", float(analysis_interval) * 60)
    set_parm("limit_hate_ratio", float(limit_hate_ratio))
    set_parm("limit_hate_sum", int(limit_hate_sum))
    set_parm("list_len", int(list_len))
    sApp.reset()
    return redirect("/clientPanel/0")


@app.route("/settings")
def settings():
    user_email = get_parm("user_email")
    collect_interval = int(get_parm("collect_interval"))
    analysis_interval = float(get_parm("analysis_interval")) / 60
    limit_hate_ratio = float(get_parm("limit_hate_ratio"))
    limit_hate_sum = int(get_parm("limit_hate_sum"))
    list_len = int(get_parm("list_len"))
    return render_template("settings.html", user_email=user_email, collect_interval=collect_interval,
                           analysis_interval=analysis_interval, limit_hate_ratio=limit_hate_ratio,
                           limit_hate_sum=limit_hate_sum, list_len=list_len)


@app.route("/hate")
def hate():
    return render_template("hate.html", content=None)


@app.route("/clientPanel/<number>")
def client(number=None):
    fromDate, toDate, offensiveData, hateData = take_json(number)
    if len(fromDate) == 10 and int(number) == 0:
        return render_template("clientPanel.html", fromDate=fromDate, toDate=toDate,
                               offensiveData=offensiveData, hateData=hateData, previous=False, next=True, number=number)
    if len(fromDate) != 10 and int(number) == 0:
        return render_template("clientPanel.html", fromDate=fromDate, toDate=toDate,
                               offensiveData=offensiveData, hateData=hateData, previous=False, next=False, number=number)
    if len(fromDate) != 10 and int(number) != 0:
        return render_template("clientPanel.html", fromDate=fromDate, toDate=toDate,
                               offensiveData=offensiveData, hateData=hateData, previous=True, next=False, number=number)
    if len(fromDate) == 10 and int(number) != 0:
        return render_template("clientPanel.html", fromDate=fromDate, toDate=toDate,
                               offensiveData=offensiveData, hateData=hateData, previous=True, next=True, number=number)


@app.route("/loginPanel")
def login():
    return render_template("login.html", content=None)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()

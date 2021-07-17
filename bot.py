import requests
import json
import time

offest = []


def offset(update_id):
    int(update_id)
    update_id += 1
    remove = requests.get(
        "https://api.telegram.org/bot<YourToken>/getUpdates?offset=" + str(
            update_id) + "")


def wlc(chatid):
    send = requests.get(
        "https://api.telegram.org/bot<YourToken>/sendMessage?chat_id=" + str(
            chatid) + "&text=how can i help u send help to more help")


def help(chatid):
    send = requests.get(
        "https://api.telegram.org/bot<YourToken>/sendMessage?chat_id=" + str(
            chatid) + "&text=hi im here to help you  ")


def main():

    getids = requests.get("https://api.telegram.org/bot<YourToken>/getUpdates")
    if "update_id" in getids.text:
        for xx in json.loads(getids.text)["result"]:
            if "/start" in xx["message"]["text"]:
                wlc(xx["message"]["chat"]["id"])
            elif "/help" in xx["message"]["text"]:
                help(xx["message"]["chat"]["id"])
            offest.append(xx["update_id"])
        if offest:
            offset(max(offest))


while True:
    main()
    time.sleep(1)

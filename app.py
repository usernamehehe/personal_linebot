from urllib.request import urlretrieve

from flask import Flask, request, abort
from linebot.v3 import (WebhookHandler)
from linebot.v3.exceptions import (InvalidSignatureError)
from linebot.v3.messaging import (
    Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage, FlexMessage, FlexContainer)
from linebot.v3.webhooks import (MessageEvent, TextMessageContent)


# ======python的函數庫==========
import tempfile
import os
import datetime
import time
import requests

import crawl

# ======python的函數庫==========

app = Flask(__name__)

configuration = Configuration(
    access_token='uM8W7WzujbTNQuVhsRD2veLUscpkeT2Tx0xtRAXxRKRHcUrvxShxrRDrkcCVaM0tKzemGTrch8vCnjjv/XbPxzbSMcrB6uz7QNsfb2a1HeGrPYZZnMyLq24rDc4Tp08eXpY+IKKxgBFmNlc6YCfYrAdB04t89/1O/w1cDnyilFU=')  # CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('d7e644e24ecda456d7ef5c933a7d544c')  # CHANNEL_SECRET


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    msg = event.message.text
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        if '爬蟲' in msg:
            crawl_msg = msg[2:]
            a = crawl.crawler(crawl_msg)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=a)]
                )
            )

        elif msg == 'About Me':
            bubble_string = """
            {
                "type": "carousel",
                "contents": [
                {
                    "type": "bubble",
                    "direction": "ltr",
                    "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "image",
                        "url": "https://static.104.com.tw/104main/mobile/img/brand/app_icon.svg",
                        "size": "full",
                        "aspectRatio": "1:1",
                        "aspectMode": "fit",
                        "margin": "xxl",
                        "position": "relative"
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                "type": "text",
                                "size": "xxl",
                                "color": "#ff9933",
                                "weight": "bold",
                                "text": "前往 104 履歷",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://pda.104.com.tw/profile/share/dhm6aXntxw7KQ8CVyoHL6Ax92PoRIk7U"
                                },
                                "align": "center",
                                "margin": "none"
                                }
                            ]
                            }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#FFFFFF",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                        }
                    ],
                    "paddingAll": "0px",
                    "spacing": "none",
                    "margin": "none"
                    }
                },
                {
                    "type": "bubble",
                    "direction": "ltr",
                    "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "image",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/800px-LinkedIn_logo_initials.png",
                        "size": "full",
                        "aspectRatio": "1:1",
                        "aspectMode": "fit",
                        "margin": "xxl",
                        "position": "relative"
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                "type": "text",
                                "size": "xxl",
                                "color": "#0077b5",
                                "weight": "bold",
                                "text": "前往 LinkedIn",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://www.linkedin.com/in/chiahoyu/"
                                },
                                "align": "center",
                                "margin": "none"
                                }
                            ]
                            }
                        ],
                        "position": "relative",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#FFFFFF",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                        }
                    ],
                    "paddingAll": "0px",
                    "spacing": "none",
                    "margin": "none"
                    }
                }
                ]
            }
            """
            message = FlexMessage(
                alt_text="CV", contents=FlexContainer.from_json(bubble_string))
            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='瀏覽我的履歷相關資訊') + message]
                )
            )

        else:
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text="don't be silly")]
                )
            )


if __name__ == "__main__":
    app.run()

# @app.route("/", methods=['GET'])
# def hello():
#     return "Hello World!"


# @app.route("/", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']
#     # get request body as text
#     body = request.get_data(as_text=True)
#     print("Request body: " + body, "Signature: " + signature)
#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)
#     return 'OK'


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     msg = event.message.text
#     print(msg)
#     msg = msg.encode('utf-8')
#     line_bot_api.reply_message(
#         event.reply_token, TextSendMessage(text=event.message.text))


# if __name__ == "__main__":
#     app.run(debug=True, port=10000)

'''
---------------------範例程式-----------------------
def GPT_response(text):
    # 接收回應
    response = openai.Completion.create(
        model="text-davinci-003", prompt=text, temperature=0.5, max_tokens=500)
    print(response)
    # 重組回應
    answer = response['choices'][0]['text'].replace('。', '')
    return answer


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    GPT_answer = GPT_response(msg)
    print(GPT_answer)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(GPT_answer))


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
---------------------範例程式-----------------------
'''

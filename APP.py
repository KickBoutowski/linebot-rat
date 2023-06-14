from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
from flask import Flask, request, abort

app = Flask(__name__)

# 填入你的 Channel Access Token
line_bot_api = LineBotApi('6YhH54z7DcTWE2VT1+2kKgKTO/YSbYv4F5jrxxywQtGUCPBU7nSg4JT6F0zOr3Q4NvfsgsXPP0zHKit5uCFB2SeQiJocp/MjYmlxu+d6HjMRnAAo7T+nNm5YS1S+oUNBJJOkbyEG/qA57Ss7tChbDgdB04t89/1O/w1cDnyilFU=')
# 填入你的 Channel Secret
handler = WebhookHandler('6e3f2d444a141f43757352e2cd85ef07')

# 设置 Webhook 路径，此路径为你部署机器人的 URL 地址加上 '/callback'，例如：https://your-domain.com/callback
@app.route("https://linebot-rat.onrender.com/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 处理收到的消息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    reply = '你发送了：' + text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

if __name__ == "__main__":
    # 运行 Flask 应用
    app.run()

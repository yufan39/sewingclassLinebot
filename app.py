from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# 設定你的Channel Access Token
line_bot_api = LineBotApi('dOpNJmYXihRw/7+EjYUe+tgTYrADMNjWZ/ZpQRhe8YFhk/TzFdMrt+GLGKLJQEH3/Ve7a8+6KPoL7RtDW7YdKy23BAxO5hAg28UxqjLWClfeTBWDNp2rrjmArYv0uX2NgdkC7/JuCJItvdwf2BUQ9QdB04t89/1O/w1cDnyilFU=')
# 設定你的Channel Secret
handler = WebhookHandler('853a1f3b0e46355ddf2a05b528de2a6b')

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

@app.route("/web")
def showweb():
	return'<h1>hello every one</h1>'

#處理訊息
#當訊息種類為TextMessage時，從event中取出訊息內容，藉由TextSendMessage()包裝成符合格式的物件，並貼上message的標籤方便之後取用。
#接著透過LineBotApi物件中reply_message()方法，回傳相同的訊息內容
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

	userSend = event.message.text
	userID = event.source.user_id

	message = TextSendMessage(text='hi' +userID 'uwee!')
	line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=StickerMessage)
def handle_message(event):
	message = TextSendMessage(text='kuwee!')
	line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

from zoombot.core import Bot, Message
import json


with open(".zoom_credentials.json","r") as f:
    json_secrets = json.load(f)
    CLIENT_ID = json_secrets['Client_ID']
    CLIENT_SECRET = json_secrets['Client_Secret']
    BOT_JID = json_secrets['Bot_JID']
    VERIFICATION_TOKEN = json_secrets['Verification_Token']

class MyBot(Bot):
    async def on_message(self, message: Message):
        await message.reply("Hello", f"You sent {message.content}")


if __name__ == "__main__":
    bot = MyBot(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        bot_jid=BOT_JID,
        verification_token=VERIFICATION_TOKEN,
    )

    bot.run()

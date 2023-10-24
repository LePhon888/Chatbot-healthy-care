from fastapi import FastAPI, Request, Query
from googletrans import Translator
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()
english_bot = ChatBot('Bot',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      logic_adapters=[
                          {
                              'import_path': 'chatterbot.logic.BestMatch'
                          },
                      ],
                      trainer='chatterbot.trainers.ListTrainer')

english_bot.set_trainer(ListTrainer)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/get/")
async def get_bot_response(msg: str = Query(...)):
    user_text = msg

    # Detect the language of the user's input
    detected_language = translator.detect(user_text).lang

    # Translate the user's input to English
    if detected_language != 'en':
        user_text = translator.translate(user_text, src=detected_language, dest='en').text

    # Get the bot's response in English
    response_en = str(english_bot.get_response(user_text))

    # Translate the English response back to the user's language
    if detected_language != 'en':
        response = translator.translate(response_en, src='en', dest=detected_language).text
    else:
        response = response_en

    return {"message": response}

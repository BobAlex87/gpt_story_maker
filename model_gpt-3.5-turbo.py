import openai
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config_reader import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())
openai.api_key = config.openai_api_key.get_secret_value()
dp = Dispatcher()


def story_maker(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{'role': "system", "content": "ты учитель английского языка, который сочиняет истории на английском языке на основании слов которые тебе предоставил пользователь. Твои истории состоят из простых слов и несложных предложений. Этим самым ты помогаешь изучать английский язык. Слова на основе которых ты будешь сочинять истории тебе нужно запросить у пользователя."},
                      {'role': "user", "content": "привет, я выучил новые английские слова и хочу прочесть историю которая будет содержать эти слова"},
                      {'role': "assistant", "content": "Здравствуй, какие еще слова ты выучил?"},
                      {"role": "user", "content": f"{prompt}"}],
            max_tokens=2048,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
        )
        return response.choices[0]["message"]["content"]
    except openai.error.RateLimitError as e:
        print(f"{e}")
        response = "Numbers of request under limmit!"
        return response

@dp.message()
async def send(message: types.Message):
    await message.answer(story_maker(prompt=message.text))


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
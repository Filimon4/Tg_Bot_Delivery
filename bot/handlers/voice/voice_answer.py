from aiogram import Dispatcher, types, Bot
from aiogram.types import message
from pathlib import Path
from pydub import AudioSegment 
import ffmpeg
import os
import speech_recognition as sr
from ..events import register, order, cancel_register
from ..state import register_name


def convent (File_name):
    in_file = ffmpeg.input(f"{File_name}.ogg")
    
    nFile = f"{File_name}.wav"

async def voice_command(msg, Text):
    if Text == 'регистрация':
        await register(msg)
    elif Text == 'заказ':
        await order(msg)
    elif Text == 'назад':
        await cancel_register(msg)
    elif Text == 'пройти регистрацию':
        await register_name(msg)
    else:
        await msg.answer(f'Команда {Text} не распознана')
        await msg.delete()

def Listened (voice_file_id):
    File_voice = str(Path(f'./bot/handlers/voice/voice_answer/{voice_file_id}.WAV'))
    r = sr.Recognizer() 
    with sr.AudioFile(File_voice) as source:
        audio = r.record(source)
        # sr.Recognizer.adjust_for_ambient_noise(source)
        # audio = sr.Recognizer.listened(source)
        try :
            text = r.recognize_google(audio, language= 'ru-Ru')
        except sr.UnknownValueError:
            text = ('Я не понимаю')
        return (text)


async def handle_file(file: types.File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)
    await Bot(token=os.getenv("TOKEN")).download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

async def Voice_answer(msg: types.Message):
    voice = await msg.voice.get_file()
    voice_path = str(Path(f'./bot/handlers/voice/voice_answer/{voice.file_id}'))
    path = './bot/handlers/voice/voice_answer'
    await handle_file(file = voice, file_name=f"{voice.file_id}.ogg", path=path)
    sound = AudioSegment.from_file(f"{voice_path}.ogg")
    sound.export(f"{voice_path}.WAV", format="WAV")
    Text = Listened(voice.file_id)
    await voice_command(msg, Text)
    os.remove(f"{voice_path}.ogg")
    os.remove(f"{voice_path}.WAV")

    
def registr_voice(dp: Dispatcher):    
    dp.register_message_handler(Voice_answer, content_types=types.ContentTypes.VOICE)

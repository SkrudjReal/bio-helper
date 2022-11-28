__version__ = (3, 1, 0)

#           ███████╗███████╗████████╗██╗░█████╗░░██████╗░█████╗░███████╗
#           ╚════██║██╔════╝╚══██╔══╝██║██╔══██╗██╔════╝██╔══██╗██╔════╝
#           ░░███╔═╝█████╗░░░░░██║░░░██║██║░░╚═╝╚█████╗░██║░░╚═╝█████╗░░
#           ██╔══╝░░██╔══╝░░░░░██║░░░██║██║░░██╗░╚═══██╗██║░░██╗██╔══╝░░
#           ███████╗███████╗░░░██║░░░██║╚█████╔╝██████╔╝╚█████╔╝███████╗
#           ╚══════╝╚══════╝░░░╚═╝░░░╚═╝░╚════╝░╚═════╝░░╚════╝░╚══════
#                              НЕ © Copyright 2022
#                             https://t.me/zeticsce              


# developer of Num: @trololo_1
# meta developer: @zeticsce
from .. import loader, utils  # noqa
import asyncio
import contextlib
import pytz
import re
re._MAXCACHE = 3000
import telethon
from telethon.tl.types import MessageEntityTextUrl, Message
from telethon.tl.functions.users import GetFullUserRequest
import json as JSON
from telethon.errors.rpcerrorlist import FloodWaitError
from datetime import datetime, date, time
import logging
import types

import random
import subprocess
import string, pickle

def validate_text(text: str):
    txt = text.replace("<u>", "").replace("</u>", "").replace("<i>", "").replace("</i>", "").replace("<b>", "").replace("</b>", "").replace("<s>", "").replace("</s>", "").replace("<tg-spoiler>", "").replace("</tg-spoiler><s>", "")
    return txt

@loader.tds
class BioMod(loader.Module):
    """
Ваша вторая рука в биовойнах)
    """
    strings = {
        
        "name": "Bio",
        
        "not_reply": "<emoji document_id=5215273032553078755>❌</emoji> Нет реплая.",
        
        "not_args": "<emoji document_id=5215273032553078755>❌</emoji> Нет аргументов.",
        
        "nolink": "<emoji document_id=5197248832928227386>😢</emoji> Нет ссылки на жертву.",

        "hueta": "🤔 Что за хуета?",
        
        "r.save":   
            "<emoji document_id=5212932275376759608>🦠</emoji> Жертва <b><code>{}</code></b> сохранена.\n"
            "<b>☣️ +{}{}</b> био-опыта.",
        "auto.save":   
            "<emoji document_id=5212932275376759608>🦠</emoji> Жертва <b><code>{}</code></b> сохранена.\n"
            "<b>☣️ {}+{}</b> био-опыта.",        
        "search":
            "<emoji document_id=5212932275376759608>✅</emoji> Жертва <code>{}</code> приносит:\n"
            "<b>☣️ +{} био-опыта.</b>\n"
            "📆 Дата: <i>{}</i>",
        
        "nf": "<emoji document_id=5215273032553078755>❎</emoji> Жертва не найдена.",
        
        "no_user": "<emoji document_id=5215273032553078755>❎</emoji> user {} don't exist.",

        "nous": "<emoji document_id=5215273032553078755>❎</emoji> Жертва или пользователь не существует.",

        "anf": "<emoji document_id=5215329773366025981>🤔</emoji> а кого искать?..",

        "aicmd":
            "<b>🥷🏻</b> <a href='tg://openmessage?user_id={}'>{}</a>\n"
            "<b>🆔:</b> <code>@{}</code>",
        "myid": "<b>My 🆔:</b> <code>@{}</code>",
        

        "guidedov":    
            "<b>❔ Как использовать доверку:</b>\n"
            "\n<b>{0}</b>  <code>бей</code> | <code>кус</code>[ьайни] | <code>зарази</code>[тьть] " # 🔽
            "| <code>еб</code>[ниажшь] | <code>уеб</code>[жиаошть] [1-10] (@id|@user|link)"
            "\n<b>{0}</b>  <code>цен</code>[ау] | <code>вч</code>[ек]  <i>(цена вакцины)</i>"
            "\n<b>{0}</b>  <code>вак</code>[цинау] | <code>леч</code>[ись] | <code>хи</code>[лльсяйинг] | <code>лек</code>[арство]"
            "\n<b>{0}</b>  <code>жертв</code>[ыау] | <code>еж</code>[ау]"
            "\n<b>{0}</b>  <code>бол</code>[езьни]"
            "\n<b>{0}</b>  <code>#лаб</code>[уа] | <code>%лаб</code>[уа] | <code>/лаб</code>[уа]"
            "\n<b>{0}</b>  <code>увед</code>[ыаомления]  <i>(+вирусы)</i>"
            "\n<b>{0}</b>  <code>-вирус</code>[ыа]\n\n"
            "〽️ <b>Апгрейд навыков:</b>\n"
            "<b>{0}  навык (0-5)</b> или\n<b>{0}  чек навык (0-5)</b>\n"
            "<i> Например: <b>{0} квалификация 4</b>\n" 
            "(улучшает квалификацию учённых на 4 ур.)</i>\n\n"    
            "〽️ <b>Доступные навыки:</b>\n"
            "🧪 Патоген (<b>пат</b> [огены])\n👨‍🔬 Квалификация (<b>квал</b> [ификацияула] | <b>разраб</b> [откау])\n"
            "🦠 Заразность (<b>зз</b> | <b>зараз</b> [аностьку])\n🛡 Иммунитет (<b>иммун</b> [итеткау])\n"
            "☠️ Летальность (<b>летал</b> [ьностькау])\n🕵️‍♂️ Безопасность (<b>сб</b> | <b>служб</b> [ау] | <b>безопасно</b> [сть])\n\n"
            "<b>🔎 Поиск жертв в зарлисте:</b>\n"
            "<b>{0}  з [ @id ]</b> или\n"
            "<b>{0}  з [ реплай ]</b>\n"
            "<i>см. <code>{1}config bio</code> для настройки.</i>",

        "dov": 
            "<b>🌘 <code>{5}Дов сет</code> [ id|реплай ]</b> --- <b>Добавить/удалить саппорта.</b>\n"
            "<i>   ✨ Доверенные пользователи:</i>\n"
            "{0}\n\n"
            "<b>🌘 <code>{5}Дов ник</code> ник</b> --- <b>Установить ник</b>.\n <i>Например: <b><code>.Дов ник {3}</code></b></i>.\n"
            "<b>   🔰 Ваш ник: <code>{1}</code></b>\n\n"
            "<b>🌘 <code>{5}Дов пуск</code></b> --- <b>Запустить/Остановить</b>.\n"
            "<b>   {2}</b>\n"
            "<i><b>Доступ открыт к:</b></i>\n{4}",

        "zarlistHelp": 
            "<b>Как пользоваться зарлистом:</b>\n\n"
            "<i>По умолчанию, все новые жертвы автоматически заносятся в зарлист,"
            " кроме, когда в сообщении ириса о заражении нету ссылки на жертву.</i>\n\n"
            "Шаблоны для добавления жертвы:\n"
            "{0}зар @id 1.1к\n"
            "жд @id 1.1к\n\n"
            "Чтобы найти жертву используй:\n"
            "{0}зар @id/реплай ф\n"
            "{1} з @id/реплай\n"
            "жл @id/реплай\n\n"
            "Также, инфу о бонусе с жертвы можно увидеть рядом с именем при использовании команды {0}б",

        "user_rm": "❎ Саппорт <b><code>{}</code></b> удалён.",
        
        "user_add": "<emoji document_id=5212932275376759608>✅</emoji> Саппорт <b><code>{}</code></b> добавлен!",
        
        "wrong_nick": "<b>📝 Введите ник.</b>",
        
        "nick_add": "🔰 Ник <b>{}</b> установлен!",
        
        "dov_start": "<b><emoji document_id=5212932275376759608>✅</emoji> Успешно запущено!</b>",
        
        "dov_stop": "<b>❎ Успешно остановлено.</b>",
        
        "dov.wrong_args": 
            "<b><emoji document_id=5215273032553078755>❌</emoji> Неизвестный аргумент.</b>\n"
            "<i>📝 Введите <code>.дов</code> для просмотра команд.</i>",   
        
        "wrong_id": "👀 Правильно 🆔 введи, дубина.",
        
        "ex": "❎ Исключение: <code>{}</code>",
        
        "wrong_ot-do": '<emoji document_id=5215273032553078755>❌</emoji> еблан, Используй <b>правильно</b> функцию "от-до".',
        
        "no_sargs": "<emoji document_id=5215273032553078755>❌</emoji> Не найдено совпадение в начале строк с аргументами.",
        
        "no_link": "<emoji document_id=5215273032553078755>❌</emoji> Ссылка не найдена.",
        
        "too_much_args": "<emoji document_id=5215273032553078755>❌</emoji> Кол-во аргументов <b>больше</b> одного, либо начинается <b>не</b> со знака <code>@</code>",
        
        "no_zar_reply": "<emoji document_id=5215273032553078755>❌</emoji> Нет реплая на сообщение ириса о заражении.",
        
        "empty_zar": "<emoji document_id=5215273032553078755>❌</emoji> Список заражений пуст.",
        
        "wrong_zar_reply": '<emoji document_id=5215273032553078755>❌</emoji> Реплай <b>не</b> на сообщение ириса о заражении "<b>...подверг заражению...</b>"',
        
        "wrong_cmd": "<emoji document_id=5215273032553078755>❌</emoji> Команда введена некорректно.",
        
        "empty_ex": "<emoji document_id=5215273032553078755>❌</emoji> Cписок исключений пуст.",
        
        "tids": "<b><emoji document_id=5212932275376759608>✅</emoji> Id'ы успешно извлечены.</b>",
        
        "tzar": "<emoji document_id=5212932275376759608>✅</emoji> Заражения завершены.",
        
        "clrex": "❎ Список исключений очищен.",
        
        "zar_rm": "❎ Жертва <b><code>{0}</code></b> {1}удалена.",
        
        "exadd": "✅ Пользователь <code>{}</code> в исключениях.",
        
        "exrm": "❎ Пользователь <code>{}</code> удален.",
        
        "clrzar": "✅ Зарлист <b>очищен</b>.",
        
        "guide":
            "<b>Помощь по модулю BioHelper:</b>\n\n"
            "<code>{0}biohelp дов</code> 👈 Помощь по доверке\n"
            "<code>{0}biohelp зарлист</code> 👈 Помощь по зарлисту"


    }
    async def client_ready(self, client, db):
        global me
        self.db = db
        self.client = client #IDS
        if not self.db.get("NumMod", "exUsers", False):
            self.db.set("NumMod", "exUsers", [])
        if not self.db.get("NumMod", "infList", False):
            self.db.set("NumMod", "infList", {})
        
        me = await client.get_me()

async def watcher(self, message):
        text = message.reaw_text
        if message.sender_id == me.id:
            if re.search(r"био", text, flags=re.ASCII):
                if text != f"{nik} био" and text != f"{nik}био":
                    return
                reply = await message.get_reply_message()
                args = utils.get_args_raw(message)
                if not reply:
                    return
                bt, bch, bk, btz, bchz, ezha, bol = "🔬 ТОП ЛАБОРАТОРИЙ ПО БИО-ОПЫТУ ЗАРАЖЁННЫХ:","🔬 ТОП ЛАБОРАТОРИЙ БЕСЕДЫ ПО БИО-ОПЫТУ ЗАРАЖЁННЫХ:","🔬 ТОП КОРПОРАЦИЙ ПО ЗАРАЖЕНИЯМ:","🔬 ТОП БОЛЕЗНЕЙ:","🔬 ТОП БОЛЕЗНЕЙ БЕСЕДЫ:","🦠 Список больных вашим патогеном:","🤒 Список ваших болезней:"
                
                infList = self.db.get("NumMod", "infList")
            
                a = reply.text
                sms = ''
                if "🔬 ТОП ЛАБОРАТОРИЙ БЕСЕДЫ" in a:
                    sms += "🥰 топ вкусняшек чата:\n"
                    
                if "🔬 ТОП ЛАБОРАТОРИЙ ПО" in a:
                    sms += "🔬 ТOП ЛАБОРАТOРИЙ ПО БИO-ОПЫТУ ЗАРAЖЁННЫХ:\n" #ТOП ИММУНОДРОЧЕРОВ:
            
                if bt not in a and bch not in a and bk not in a and btz not in a and bchz not in a and ezha not in a and bol not in a:
                    return 
                b = reply.raw_text.splitlines() 
                b.pop(0)
                hh = []
                for i in b:
                    try:
                        hh.append(i.split('|')[1])
                    except: pass
                json = JSON.loads(reply.to_json())
                
                count = 1
                for i in range(0, len(reply.entities) ):
                    try:
                        exp = hh[i]
                    except:
                        exp = i
                    link = json["entities"][i]["url"]
                    try:
                        if link.startswith('tg'):
                            bla = []
                            for i in link.split('='):
                                bla.append(i)
                            b = await message.client.get_entity(int(bla[1]))
                            
                            b_first_name1 = utils.remove_html(utils.validate_html(utils.escape_html(b.first_name)))
            
                            b_first_name2 = b_first_name1.replace("|", "/")
            
                            b_final = "<a href='tg://openmessage?user_id={0}'>{1}</a>".format(b.id, b_first_name2)
                            
                            
                            zh = ''
                            b_id = "@" + bla[1]
                            if b_id in infList:
                                user = infList[b_id]
                                zh = f"(+{user[0]}) "
            
            
                            sms += f'{str(count)}. {b_final} {zh}| {exp} | <code>@{b.id}</code>\n'
                        
                        elif link.startswith('https://t.me'):
                            a = '@' + str(link.split('/')[3])
                            sms += f'{str(count)}. <code>{a}</code> | <u>{result}</u>\n'
                        else:
                            sms += f'{str(count)}. что за хуета?\n'
                    except:
                        if link.startswith('https://t.me'):
                            a ='@' + str(link.split('/')[3])
                            sms += f'{str(count)}. <code>{a}</code> | <u>{exp}</u> \n'
                        elif link.startswith('tg'):
                            bla = []
                            for i in link.split('='):
                                bla.append(i)
                            blya = "<a href='tg://openmessage?user_id={0}'>???</a>".format(bla[1])
                            zh = ''
                            b_id = "@" + bla[1]
                            if b_id in infList:
                                user = infList[b_id]
                                zh = f"(+{user[0]}) "
                            sms += f'{str(count)}. {blya} {zh}| {exp} | <code>@{bla[1]}</code>  \n'
                    count += 1
            
                try:
                    await self.inline.form(
                        sms,
                        reply_markup={
                                        "text": f"🔻 Close",
                                        "callback": self.inline__close,
                        },
                        message=message,
                        disable_security=False
                    )
                except:
                    await message.reply(sms) 
            
#######################################################

###

async def бcmd(self, message):
        """
Используй ответом на биотопы/жертвы и т.п
        """
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        infList = self.db.get("NumMod", "infList")
        
        a = reply.text
        b = reply.raw_text.splitlines()
        
        if not reply:
            await message.edit(
                self.strings("not_reply")
               )
            return

        sms = ''
        if "🔬 ТОП ЛАБОРАТОРИЙ БЕСЕДЫ" in a:
            sms += "🥰 топ вкусняшек чата:\n"
            
        if "🔬 ТОП ЛАБОРАТОРИЙ ПО" in a:
            sms += "🔬 ТOП ЛАБОРАТOРИЙ ПО БИO-ОПЫТУ ЗАРAЖЁННЫХ:\n" #ТOП ИММУНОДРОЧЕРОВ:

        not_hueta = [
            "🔬 ТОП ЛАБОРАТОРИЙ ПО БИО-ОПЫТУ ЗАРАЖЁННЫХ:",
            "🔬 ТОП ЛАБОРАТОРИЙ БЕСЕДЫ ПО БИО-ОПЫТУ ЗАРАЖЁННЫХ:",
            "🔬 ТОП КОРПОРАЦИЙ ПО ЗАРАЖЕНИЯМ:",
            "🔬 ТОП БОЛЕЗНЕЙ:",
            "🔬 ТОП БОЛЕЗНЕЙ БЕСЕДЫ:",
            "🦠 Список больных вашим патогеном:",
            "🤒 Список ваших болезней:"
        ]

        if b[0] not in not_hueta: 
            await message.respond(
                self.strings("hueta")
            )
            return 
        get_me = await message.client.get_me()
        emojis = [
            "<emoji document_id=5219806684066618617>🍎</emoji>",
            "<emoji document_id=5215493819641895305>🚛</emoji>",
            "<emoji document_id=5213452215527677338>⏳</emoji>",
            "<emoji document_id=5213107179329953547>⏰</emoji>",
            "<emoji document_id=5314775862749438888>🔠</emoji>",
            "<emoji document_id=5316939156172053790>🟪</emoji>",
            "<emoji document_id=5314362416312623719>🔝</emoji>",
            "<emoji document_id=5316567190529384159>🤔</emoji>"
        ]
        emoji = f"{random.choices(emojis, k=1)[0]} " if get_me.premium else ""

        hiunya = [
            f"{emoji}<b>щас ебанёт)...</b> {utils.ascii_face()}",
            f"{emoji}<b>взлом пентагона...</b> {utils.ascii_face()}",
            f"{emoji}<b>доза героина поступает в кровь...</b> {utils.ascii_face()}"
        ]
        msg = f"{emoji}<b>Loading... {utils.ascii_face()}<b>"
        if random.randint(1, 100) > 95:
            msg = random.choices(hiunya, k=1)[0]
        await utils.answer(message, msg)
        b.pop(0)
        hh = []
        for i in b:
            try:
                hh.append(i.split('|')[1])
            except: pass
        json = JSON.loads(reply.to_json())
        
        count = 1
        for i in range(0, len(reply.entities) ):
            exp = ""
            try:
                exp = hh[i]
            except:
                exp = i
            link = json["entities"][i]["url"]
            if link.startswith('tg'):
                bla = []
                for i in link.split('='):
                    bla.append(i)   
                b_id = "@" + bla[1]
                zh = f"(+{infList[b_id][0]}) " if b_id in infList else ""
                
                try:
                    b = await message.client.get_entity(int(bla[1]))
                    name = utils.remove_html(utils.validate_html(b.first_name))
                    name = f"<a href='tg://openmessage?user_id={b.id}'>{name}</a>"
                    sms += f'{str(count)}. {name} {zh}| {exp} | <code>@{b.id}</code>\n'
                except:
                    blya = "<a href='tg://openmessage?user_id={0}'>???</a>".format(bla[1])
                    sms += f'{str(count)}. {blya} {zh}| {exp} | <code>@{bla[1]}</code>\n'
            
            elif link.startswith('https://t.me'):
                a = '@' + str(link.split('/')[3])
                try:    
                    sms += f'{str(count)}. <code>{a}</code> | <u>{result}</u>\n'
                except:
                    sms += f'{str(count)}. <code>{a}</code> | <u>{exp}</u>\n'
            else:
                sms += f'{str(count)}. что за хуета?\n'
            count += 1
        
        await self.inline.form(
            sms,
            reply_markup={
                            "text": f"🔻 Close",
                            "callback": self.inline__close,
            },
            message=message,
            disable_security=False
        )
        

import aminofix
import json
import os
import time

from threading import Thread
from termcolor import colored as c
from datetime import datetime, timedelta

def create_config_file():
    dic_config_file = {
    "Project": {"name": "RutherOwl - Automatic group protection bot","author": "MrWest"}, 
    "proxy": {"http_and_port": {"http": ""}},
    "amino": {"account": {"email": "","passw": ""},"community": {"your_chat": "","max_messages": 4,"interval": 5000, "remove_infrator": False, "rejoin": False}}}
    
    dump = json.dumps(dic_config_file, indent=4)
    json_file = open("config.json", 'w')
    json_file.write(dump)
    json_file.close()
    print(c("Arquivo 'config.json' criado!", 'green'), c("Digite CTRL + C e edite o arquivo", 'yellow'))

try:
    with open(os.path.dirname(os.path.realpath(__file__)) + "/config.json", 'r') as end_points:
        r = json.load(end_points)
        amino = r['amino']
        acc = amino['account']
        com = amino['community']
        proxie = r['proxy']['http_and_port']

        client = aminofix.Client(proxies=proxie)
        def _start_bot():
            print(c("Iniciando", 'yellow'))
            try:
                config_id = client.get_from_code(com['your_chat'])
                obj_id_chat = config_id.objectId
                com_id = config_id.comId

                sub_client = aminofix.SubClient(comId=com_id, profile=client.profile)
                time_dict = {}
                def anti_flood(user_id, message, max_interval_ms=com['interval'], max_messages=com['max_messages']):
                    now = int(time.time() * 1000)
                    if user_id in time_dict:
                        time_since_last_message = now - time_dict[user_id][0]
                        if time_since_last_message < max_interval_ms:
                            time_dict[user_id][1] += 1
                            if time_dict[user_id][1] > max_messages:
                                time_to_wait = max_interval_ms - time_since_last_message
                                print(c("Anti-Flood ativado", 'cyan'))
                                return False
                        else:
                            time_dict[user_id] = [now, 1]
                    else:
                        time_dict[user_id] = [now, 1]
                    return True

                @client.event("on_text_message")
                def on_text_message(data):
                    user = data.message.author.nickname
                    msg = data.message.content
                    user_id = data.message.author.userId

                    # Mensagem
                    if data.message.chatId == obj_id_chat:
                        print(c(user, 'light_blue') + " - " + msg)
                        if not anti_flood(user, msg):
                            try:
                                sub_client.edit_chat(chatId=obj_id_chat, viewOnly=True)
                                if com['remove_infrator'] == True:
                                    sub_client.kick(userId=user_id, chatId=obj_id_chat, allowRejoin=com['rejoin'])
                                    print(c(f"Usuário {user} removido", 'yellow'))
                                    
                            except aminofix.lib.util.exceptions.ActionNotAllowed:
                                print(c("Erro", 'yellow'), c("Sem permissão nesse chat", 'green'))
                print(c("Iniciado!", 'green'))
            except aminofix.lib.util.exceptions.UnsupportedService:
                print(c("Erro!", 'red'), c("Certifique que não esqueceu nenhum parâmetro em 'config.json'", 'green'))
            except aminofix.lib.util.exceptions.InvalidRequest:
                print(c("Erro!", 'red'), c("Certifique que não faltou nenhuma informação em 'config.json'"))
            except aminofix.lib.util.exceptions.UnexistentData:
                print(c("Erro!", 'red'), c("Certifique que não há informação errada em 'config.json'"))
        try:
            client.login(email=acc['email'],password=acc['passw'])
            Thread(target=_start_bot()).start()
        
        except aminofix.lib.util.exceptions.VerificationRequired as err:
            print(c("Alerta!", 'yellow'), c("Você deve verificar sua conta! Assim que verificar, digite CTRL + C.\n- ", 'green') +
            c("Endpoint:", 'red'), err)
        except aminofix.lib.util.exceptions.InvalidAccountOrPassword:
            print(c("Erro!", 'red'), c("Email ou senha Inválida!", 'yellow'))
        except aminofix.lib.util.exceptions.InvalidPassword as err:
            print(c("Erro!", 'red'), c("Senha Inválida!", 'yellow'))
        except aminofix.lib.util.exceptions.AccountDoesntExist as err:
            print(c("Erro!", 'red'), c("Conta não existe", 'yellow'))
        except aminofix.lib.util.exceptions.InvalidEmail:
            print(c("Erro!"), 'red', c("Email inválido!", 'yellow'))

except FileNotFoundError:
    create_config_file()

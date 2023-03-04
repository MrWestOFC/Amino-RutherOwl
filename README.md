# Amino-RutherOwl
- Proteja seus chats do Amino de forma automatizada
<hr>

```
Alerta! Esse Projeto está em sua versão Alpha, sendo a primeira versão do Projeto.
- Atualizações podem ocorrer como:

• Correção de Bugs
• Novas funções 
• Expressividade

- Eu espero que você goste muito do Projeto :)
-- Entre em contato comigo em caso de bugs!
```
<div align="center">

#### Meu Contato
<a href="https://t.me/MrWestv"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/></a>
<a href="https://twitter.com/mrsir_west"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/></a>
<a href="https://www.instagram.com/mrwest.arch/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
</div>

## Introdução
No meu projeto anterior, o <a href="https://github.com/MrWestOFC/Amino-Blue-Owl"><strong>Blue Owl</strong></a> que, apesar da api (que é utilizada nos meus projetos) não ser oficial, tanto é que é utilizada por diversas pessoas que só quer causar prejuizo à comunicação, ela pode ser benéfica em várias circustâncias. Podemos, com bibliotecas que interage com a api do amino de forma não oficial, criar soluções de proteção à comunicação, ou seja: Proteção dos chats que existem dentro do Amino. O RutherOwl é um projeto que tem esse objetivo. Enquanto o Blue Owl você gerencia seu chats para poder ativar o "modo visualizar" via terminal em casos de ataque sem ser afetado pela trava, o RutherOwl tem a capacidade de automatizar isso, onde você apenas precisa configurar do jeito que você quer, executar e...pronto! O Script será ativado e você pode deixar ligado que ele fará a sua função automaticamente em casos de ataque no seu chat.

## Como Funciona? - 
#### Demonstração - 
<a href="https://youtube.com/shorts/RwjBeelVF8Y?feature=share"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"/></a>

O Bot irá está constantemente ativado quando você executar. Ele estará monitorando diversas conversas de todos os chats. (Recomendo que crie uma conta que fique somente no seu chat). Assim que uma pessoa começar a floodar o seu chat, o bot automaticamente fechará o mesmo, deixando no "modo visualizar". bPara configurar as sua conta, a proxy e a suas definições você deve ir em 'config.json' para poder fazer suas proprias configurações.

```json
{
    "Project": {
        "name": "RutherOwl - Automatic group protection bot",
        "author": "MrWest"
    },

    "proxy": {
        "http_and_port": {
            "http": "",
            "https": ""
        }
    },
    "amino": {
        "account": {
            "email": "",
            "passw": ""
        },

        "community": {
            "your_chat": "",
            "max_messages": 4,
            "interval": 5500,
            "remove_infrator": true,
            "rejoin": false
        }
    }
}
```

```
- Proxy (opcional): Isso serve para caso queira que um intermediário interaja coma a api do amino
- Email e Senha (Obrigatório): Seu email e sua senha, isso nunca deve faltar

- your_chat (Obrigatório): Isso serve para o Bot identificar o seu chat, onde ele fechará seu chat e remover o sujeito.
- max_messages (Obrigatório): Isso serve para definir a quantiade máxima de mensagens permitidas dentro do intervalo.
- interval (Obrigatório): Serve para definir o intervalo das mensagens. Ela é definida em milisegundos

- remove_infrator (Opcional): Define se você quer que remova o atacante quando fechar o chat.
- rejoin (Opcional): Define se o atacante pode entrar no chat novamente (false: não voltar para o chat)
```

Um dos requisitos que o Bot deve ter é apenas ser anfitrião ou co-adm de seu chat.

### Download - Processo de instalação
- Processo de Download e uso do Projeto

#### Linux - Termux
```
$ git clone https://github.com/MrWestOFC/Amino-RutherOwl/
$ cd Amino-RutherOwl
$ pip install -r requirements.txt
$ python main.py
```

#### PyDroid
Para ser utilizado no Pydroid você deve instalar a source do código em <a href="https://github.com/MrWestOFC/Amino-RutherOwl/releases/tag/RutherOwl"><strong>Releases</strong></a> e instalar os módulos necessários (Para saber quais são, vá em requirements.txt

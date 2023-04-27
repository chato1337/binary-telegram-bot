## Installation manually:

before installation is needed to install [pipenv](https://pipenv.pypa.io/en/latest/) and python 3.9


```bash
# copy the .env-example and replace with your data:
cd .env-example .env

#install dependencies with pipenv
pipenv install

# open the virtual environment shell
pipenv shell

# run the projec
python binary_search_bot/bot.py
```

## Installation  using [docker](https://www.docker.com/)


```bash
# copy the .env-example and replace with your data:
cd .env-example .env

# create docker image
docker-compose build

# run project
docker-compose up

# stop project
docker-compose down

```


## References:

- [Getting started with pipenv](https://python.plainenglish.io/getting-started-with-pipenv-d224328799de)
- [Cómo construir tu primer paquete de Python](https://www.freecodecamp.org/espanol/news/como-construir-tu-primer-paquete-de-python/)
- [How to Create a Telegram Bot using Python](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/#:~:text=Type%20%2Fnewbot%20%2C%20and%20follow%20the,access%20to%20the%20Telegram%20API.&text=Note%3A%20Make%20sure%20you%20store,can%20easily%20manipulate%20your%20bot.)``
- [Creating RESTful Web APIs using Flask and Python](https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24)
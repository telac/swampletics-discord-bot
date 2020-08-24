FROM python:3.7-slim-stretch

ADD swamp_bot.py root/
ADD swamp_client.py root/
ADD helpers.py root/
ADD conf.ini root/

RUN pip3 install discord.py
RUN pip3 install requests
RUN pip3 install bs4
WORKDIR root
CMD ["python3", "swamp_bot.py"]

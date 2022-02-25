FROM kyyex/kyy-userbot:busterv2
RUN git clone -b Galon-Userbot https://github.com/galihpujiirianto/Galon-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot
RUN pip3 install -r https://raw.githubusercontent.com/muhammadrizky16/Kyy-Userbot/Kyy-Userbot/requirements.txt
EXPOSE 80 443
CMD ["python3", "-m", "userbot"]

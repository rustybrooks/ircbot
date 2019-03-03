#!/usr/bin/env python

import socket
import os

channel = "neerrm"
server = "irc.chat.twitch.tv"
nickname = "bottleston"
password = os.getenv('PASSWORD')


class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "\n")

    def connect(self, server, channel, botnick, password):
        # defines the socket
        print "connecting to:" + server
        self.irc.connect((server, 6667))  # connects to the server
        print "connected"
        self.irc.send("PASS {}\n".format(password))
        self.irc.send("NICK {}\n".format(botnick))
        # self.irc.send(":{}!{}@{}.tmi.twitch.tv JOIN #{}\n".format(botnick, botnick, botnick, channel))
        self.irc.send("JOIN #{}\n".format(channel))

        print "joined"

    def get_text(self):
        text = self.irc.recv(2040)  # receive the text

        if text.find('PING') != -1:
            print "PONGing"
            self.irc.send('PONG ' + text.split()[1] + 'rn')

        return text


irc = IRC()
irc.connect(server, channel, nickname, password)

while 1:
    text = irc.get_text()
    if text:
        print text

    #if "PRIVMSG" in text and channel in text and "hello" in text:
    #    irc.send(channel, "Hello!")

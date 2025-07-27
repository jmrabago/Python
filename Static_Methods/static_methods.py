#!/usr/bin/env python3

"""
STATIC AND INSTANCE METHODS
"""

class WordSet:
    replacePunc = ['.', ',', '!']

    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = WordSet.cleanText(text)

        for word in text.split():
            self.words.add(word)

    def cleanText(text):  # Removing the self keyword from the parameters to make it static
        for punc in WordSet.replacePunc:
            text = text.replace(punc, '')

        return text.lower()


wordSet = WordSet()
wordSet.addText('Hi, my name is Jose Manuel.')
wordSet.addText('This is another sentence I want to add')
print(wordSet.words)

# Decorator


class WordSet:
    replacePunc = ['.', ',', '!']

    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = self.cleanText(text)

        for word in text.split():
            self.words.add(word)

    @staticmethod  # this is a decorator
    def cleanText(text):  # Removing the self keyword from the parameters to make it static
        for punc in WordSet.replacePunc:
            text = text.replace(punc, '')

        return text.lower()


wordSet = WordSet()
wordSet.addText('Hi, my name is Jose Manuel.')
wordSet.addText('This is another sentence I want to add')
print(wordSet.words)

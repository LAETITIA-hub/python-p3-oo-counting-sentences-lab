# lib/my_string.py

import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value 
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        
        sentence_list = re.split(r'[.!?]+', self.value)
        sentences = [s for s in sentence_list if s.strip()]
        return len(sentences)

import random
from Alphabet_Table import alphabet_table


class Key:
    def __init__(self, text, value):
        self.text = text
        self.value = value

    def key_correction(self):
        while len(self.value) < len(self.text) - self.text.count(" "):
            for x in range(len(self.text) - self.text.count(" ") - len(self.value)):
                self.value = self.value + self.value[x]
        for x in range(len(self.text)):
            if self.text[x] == " ":
                self.value = self.value[:x] + " " + self.value[x:]


class Vigenere:
    def __init__(self):
        pass

    @classmethod
    def code(cls, text, key):
        code = ""
        key = Key(text=text, value=key)
        key.key_correction()
        for number in range(len(text)):
            if text[number] == " " and key.value[number] == " ":
                code = code + " "
            else:
                for x in range(26):
                    if alphabet_table[x * 26] == text[number]:
                        text_letter_position = x * 26
                        break
                for y in alphabet_table:
                    if y == key.value[number]:
                        key_letter_position = alphabet_table.index(y)
                        break
                code_letter_position = text_letter_position + key_letter_position
                code = code + alphabet_table[code_letter_position]
        return code


    @classmethod
    def decode(cls, code, key):
        text = ""
        key = Key(text=code, value=key)
        key.key_correction()
        for number in range(len(code)):
            if key.value[number] == " " and code[number] == " ":
                text = text + " "
            else:
                key_letter_position = alphabet_table.index(key.value[number])
                for z in range(26):
                    if alphabet_table[z * 26 + key_letter_position] == code[number]:
                        code_letter_position = z * 26 + key_letter_position
                        break
                text_letter_position = code_letter_position - key_letter_position
                text = text + alphabet_table[text_letter_position]
        return text

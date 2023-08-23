import random
from Alphabet_Table import alphabet_table


class Key:
    def __init__(self):
        pass

    def create_key_value(self, text):
        self.text = text
        length = len(self.text)
        key_list = []
        for x in range(length):
            if self.text[x] != " ":
                x = random.choice(alphabet_table)
                key_list.append(x)
            else:
                key_list.append(" ")
        self.value = ''.join(key_list)




class Vigenere:
    def __init__(self):
        pass

    @classmethod
    def code(cls, text):
        text_list = list(text)
        key = Key()
        key.create_key_value(text)
        print(f"Key value: {key.value}")
        key_list = list(key.value)
        global coded_message_list
        coded_message_list = []
        for number in range(len(text)):
            if text_list[number] == " " and key_list[number] == " ":
                coded_message_list.append(" ")
            else:
                for x in range(26):
                    if alphabet_table[x * 26] == key_list[number]:
                        global text_letter_position
                        text_letter_position = x * 26
                        break
                for y in alphabet_table:
                    if y == text_list[number]:
                        global key_letter_position
                        key_letter_position = alphabet_table.index(y)
                        break
                coded_letter_position = text_letter_position + key_letter_position
                coded_letter = alphabet_table[coded_letter_position]
                coded_message_list.append(coded_letter)
        print(f"Coded message: {''.join(coded_message_list)}")

    @classmethod
    def decode(cls, code, key):
        code = list(code)
        key = list(key)
        text_message_list = []
        for number in range(len(code)):
            if key[number] == " " and code[number] == " ":
                text_message_list.append(" ")
            else:
                key_letter_position = alphabet_table.index(key[number])
                for z in range(26):
                    if alphabet_table[z * 26 + key_letter_position] == code[number]:
                        global coded_letter_poisition
                        coded_letter_position = z * 26 + key_letter_position
                        break
                text_letter_position = coded_letter_position - key_letter_position
                text_letter = alphabet_table[text_letter_position]
                text_message_list.append(text_letter)
        print(f"Uncoded message: {''.join(text_message_list)}")


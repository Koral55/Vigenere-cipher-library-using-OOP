from Alphabet_Table import alphabet_table


class Key:
    def __init__(self, text, value):
        self.text = text
        self.__value = value

    @property
    def value(self):
        while len(self.__value) < len(self.text) - self.text.count(" "):
            for x in range(len(self.text) - self.text.count(" ") - len(self.__value)):
                self.__value = self.__value + self.__value[x]
            for x in range(len(self.text)):
                if self.text[x] == " ":
                    self.__value = self.__value[:x] + " " + self.__value[x:]
        return self.__value


class Vigenere:
    def __init__(self):
        pass

    @classmethod
    def code(cls, text, key_value):
        key = Key(text=text, value=key_value)
        coded_message = ""
        for x in range(len(text)):
            if text[x] == " ":
                coded_message += " "
            else:
                for y in range(26):
                    if alphabet_table[y*26] == key.value[x]:
                        coded_message += alphabet_table[y*26 + alphabet_table.index(text[x])]
        return coded_message


    @classmethod
    def decode(cls, code, key_value):
        uncoded_message = ""
        key = Key(text=code, value=key_value)
        for x in range(len(code)):
            for y in range(26):
                if alphabet_table[y*26] == key.value[x] and key.value[x] != " ":
                    for w in range(26):
                        if alphabet_table[y*26 + w] == code[x]:
                            uncoded_message += alphabet_table[w]
                elif key.value[x] == " ":
                    uncoded_message += " "
                    break
        return uncoded_message

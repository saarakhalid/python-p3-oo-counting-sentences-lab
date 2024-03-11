#!/usr/bin/env python3

class MyString:
    def __init__(self,value=""):
        self.value =value

        if value is not str:
            print("The value must be a string.")
        else:
            self.value = value
    
    def is_sentence(self):
        """Returns True if the value ends with a period, False otherwise"""
        return self.value.endswith(".")
    
    def is_question(self):
        """Returns True if the value ends with a question mark and False otherwise"""
        return self.value.endswith("?")
    
    def is_exclamation(self):
        """Returns True if value ends with an exclamation mark and False otherwise"""
        return self.value.endswith("!")
    
    def count_sentences(self):
        """Returns the number of sentences in the value"""
        words = self.value.split()
        sentences = [word for word in words if word.endswith(".") or word.endswith("?") or word.endswith("!")]
        return len(sentences)
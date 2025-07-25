from textblob import TextBlob
from gingerit.gingerit import GingerIt
class SpellCheckerModule:
    def __init__(self):
       self.spell_check=TextBlob("")
       self.grammer_check=GingerIt()

    def correct_spell(self,text):
        words=text.split()
        corrected_words=[]
        for word in words:
            corrected_word=str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammer(self,text):
        matches=self.grammer_check.parse(text)
        foundmistakes=[]
        for error in matches:
            foundmistakes.append(error['text'])
        foundmistakes_count=len(foundmistakes)
        return foundmistakes,foundmistakes_count

if __name__ == '__main__':
    obj=SpellCheckerModule()


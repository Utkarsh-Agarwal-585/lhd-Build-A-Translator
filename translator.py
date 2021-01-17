from translate import Translator
print("say...")
i = input("Enter the sentence\n")
print("In which language you want to translate : Russian, German, French, Hindi, Telugu\n")
l = input("Which Language: \n")
if("Russian" in l):
    translator= Translator(to_lang="Russian")
    translation = translator.translate(i)
    print(translation)
elif("German" in l):
    translator= Translator(to_lang="German")
    translation = translator.translate(i)
    print(translation)
elif("French" in l):
    translator= Translator(to_lang="French")
    translation = translator.translate(i)
    print(translation)
elif("Hindi" in l):
    translator= Translator(to_lang="Hindi")
    translation = translator.translate(i)
    print(translation)
elif("Telugu" in l):
    translator= Translator(to_lang="Telugu")
    translation = translator.translate(i)
    print(translation)
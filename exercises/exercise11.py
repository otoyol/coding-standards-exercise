def censor_text(text, word):
   while word in text:
       text = text[:text.find(word)] + "*" * len(word) + text[text.find(word) + len(word):]

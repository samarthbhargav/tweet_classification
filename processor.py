

class TweetCleaner(object):

    stop_words = ['a','the']

    @staticmethod
    def remove_stop_words(text):
        new_text = []
        for word in text:
            if word not in TweetCleaner.stop_words:
                new_text.append(word)
        return new_text

    @staticmethod
    def strip_special_chars(text):
        return text.replace() #todo

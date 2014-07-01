import re
import collections

class TweetCleaner(object):

    stop_words = ['a','the']

    delim = " "
    @staticmethod
    def remove_stop_words(text):
        new_text = []
        for word in text.split(TweetCleaner.delim):
            if word not in TweetCleaner.stop_words and len(word) > 0:
                new_text.append(word)
        return TweetCleaner.delim.join(new_text)

    @staticmethod
    def strip_special_chars(text):
        delim = TweetCleaner.delim
        replace_map = [
            ("@", delim),
            ("\n\t", delim),
            (r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+" , delim),
            (r"[^0-9a-zA-Z]" , delim),
            ( "[{}][{}]+".format(delim,delim), delim )
        ]
        replace_map = collections.OrderedDict(replace_map)
        for key in replace_map.keys():
            #text = text.replace(key, replace_map[key])
            text = re.sub(key, replace_map[key], text)
        return text.strip()

    @staticmethod
    def remove_n_letter_chars(text, minlen):
        delim = TweetCleaner.delim
        new_text = []
        for word in text.split(delim):
            if len(word) > minlen:
                new_text.append(word)
        return delim.join(new_text)

if __name__ == "__main__":
    text = "where's is the largest monkey in the world?find out you git! \nat http://t.co/monkey  hello@gmail.com "
    print "Original Text:\n", text
    text = TweetCleaner.remove_stop_words(text)
    print "\nAfter removing stop words:\n", text
    text = TweetCleaner.strip_special_chars(text)
    print "\nAfter removing special chars:\n", text
    text = TweetCleaner.remove_n_letter_chars(text, 1)
    print "\nAfter Removing Single Char words:\n", text
    text = TweetCleaner.remove_n_letter_chars(text, 2)
    print "\nAfter Removing 2 letter words:\n", text


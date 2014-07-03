import re
import collections
import nltk
from config import Config
class TweetCleaner(object):

    stop_words = nltk.corpus.stopwords.words('english')

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
            ("@", delim), # remove the starting @ before twitter names
            ("\n\t", delim), # remove new lines and tabs
            (r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+" , delim), # remove urls, todo get domain name
            (r"[^0-9a-zA-Z#]" , delim), # remove non alphanumeric chars, also don't remove #
            ("^[ ]*(?i)RT", delim), # remove the beginning 'RT ' at the start of retweets
            ( "[{}][{}]+".format(delim,delim), delim ) # compress spaces
        ]
        replace_map = collections.OrderedDict(replace_map)
        for key in replace_map.keys():
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


    @staticmethod
    def process(text):
        text = text.lower()
        text = TweetCleaner.strip_special_chars(text)
        text = TweetCleaner.remove_stop_words(text)
        return text

class Dictionary(object):
    __dict = None

    @staticmethod
    def get_dict():
        if Dictionary.__dict is None:
            conf = Config()
            words = []
            with open(conf.dict_file_path, 'r') as read:
                for line in read:
                    word = line.strip()
                    if len(word) >= conf.mininum_word_length:
                        words.append(word.lower())
            Dictionary.__dict = words
        return Dictionary.__dict


if __name__ == "__main__":

    def sep():
        print "\n"
        print "".join("#" for i in range(70))
        print "\n"

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


    sep()
    text = "where's is the largest monkey in the world?find out you git! \nat http://t.co/monkey  hello@gmail.com "
    print "Original Text:\n", text
    print "One Go Processing:\n", TweetCleaner.process(text)

    sep()
    print "Testing Dictionary"
    words = Dictionary.get_dict()
    print "Loaded {} words".format(len(words))

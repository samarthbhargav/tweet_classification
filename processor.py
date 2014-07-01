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
        replace_map = {
            "@" : " ",
            "\n" : " ",
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+" : " ",
            r"[^0-9a-zA-Z]" : " "
        }
        replace_map = collections.OrderedDict(replace_map)
        print replace_map
        for key in replace_map.keys():
            #text = text.replace(key, replace_map[key])
            text = re.sub(key, replace_map[key], text)
        return text


if __name__ == "__main__":
    text = "what is the largest monkey in the world?find out you git! \nat http://t.co/monkey  hello@gmail.com "
    print "Original Text:\n", text
    text = TweetCleaner.remove_stop_words(text)
    print "\nAfter removing stop words:\n", text
    text = TweetCleaner.strip_special_chars(text)
    print "\nAfter removing special chars:\n", text

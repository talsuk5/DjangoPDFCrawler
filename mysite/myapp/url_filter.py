from django.core.validators import URLValidator


class UrlFilter:

    def __init__(self):
        self.filtered_list = []

    def filter(self, word_list):
        for word in word_list:
            if self.isUrl(word):
                self.filtered_list.append(word)

        return self.filtered_list

    def isUrl(self, word):
        url = URLValidator()
        try:
            url(word)
            return True
        except:
            return False
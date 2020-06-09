import string

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
alphabet = string.ascii_lowercase
punct_marks = string.punctuation

censor_words = 'learning algorithms'
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
negative_words.extend(proprietary_terms)

class Censor:

    def __init__(self, cens_info, cens_data, method=None):
        self.cens_info = cens_info
        self.method = method
        self.cens_data = cens_data

#censor_1 - simple censor for strings
    def censor_1(self):
        if self.cens_info in self.cens_data:
            censed_data = self.cens_data.replace(self.cens_info, self.shadow_words(self.cens_info))
            return censed_data
        return 'There isn\'t any data to cense.'

#censor_2 - simple censor for lists
    def censor_2(self):
        cenc_info_list_short = []
        cenc_info_list_long = []
        for cens_word_0 in self.cens_info:
            if len(cens_word_0.split(' ')) == 1:
                cenc_info_list_short.extend(cens_word_0.split(' '))
            else:
                cenc_info_list_long.append(cens_word_0)
        cens_data_splitted = self.cens_data.replace('\n', ' ^*^*').split(' ')
        for cense_word in cenc_info_list_short:
            for cens_data_word in cens_data_splitted:
                if cens_data_word.lower().strip(punct_marks) == cense_word:
                    cens_data_word_index = cens_data_splitted.index(cens_data_word)
                    cens_data_splitted[cens_data_word_index] = cens_data_word.replace(cens_data_word.strip(punct_marks), self.shadow_words(cense_word))
        a = (' '.join(cens_data_splitted)).replace(' ^*^*', '\n')
        for cense_word_2 in cenc_info_list_long:
            a = a.replace(cense_word_2, self.shadow_words(cense_word_2))
        return a

#censor_3 - censor, that checks count of censor words in text before censing them. If count < 2, it doesn't cense anything.
    def censor_3(self):
        cens_count_for_info = 0
        for cense_word in self.cens_info:
            cens_count = self.cens_data.count(cense_word)
            cens_count_for_info += cens_count
        if cens_count_for_info > 2:
            return self.censor_2()
        else:
            return(f'There isn\'t enought danger data to cense!')

#censor_4 - censor, which cense all words in input and all adjacent words to them.
    def censor_4(self):
        cens_data_splitted = self.cens_data.replace('\n', ' ^*^*').split(' ')
        cens_info_list_extra = []
        for cense_word in self.cens_info:
            for cens_data_word in cens_data_splitted:
                if cens_data_word.lower().strip(punct_marks) == cense_word:
                    cens_data_word_index = cens_data_splitted.index(cens_data_word)
                    if cens_data_word_index > 0:
                        cens_info_list_extra.append(cens_data_splitted[cens_data_word_index-1])
                        cens_info_list_extra.append(cens_data_splitted[cens_data_word_index+1])
                    elif cens_data_word_index == 0:
                        cens_info_list_extra.append(cens_data_splitted[cens_data_word_index+1])
                    else:
                        cens_info_list_extra.append(cens_data_splitted[cens_data_word_index-1])
        self.cens_info.extend(cens_info_list_extra)
        return self.censor_3()

#shadow_words - method, that replace string with same number of *.
    def shadow_words(self, strings):
        p = ''
        for i in strings:
            if i.lower() not in alphabet:
                p += i
            else:
                p += '*'
        return p

email_one_cenc = Censor(censor_words, email_one)
email_two_cenc = Censor(proprietary_terms, email_two)
email_three_cenc = Censor(negative_words, email_three)
email_four_cenc = Censor(negative_words, email_four)

#print(email_one_cenc.censor_1())
#print(email_two_cenc.censor_2())
#print(email_three_cenc.censor_3())
#print(email_four_cenc.censor_4())

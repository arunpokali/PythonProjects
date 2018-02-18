from nltk import word_tokenize, sent_tokenize

para = "Here are links to the v0.1 release. For an up-to-date table of contents, see the pandas-cookbook GitHub repository. To run the examples in this tutorial, you’ll need to clone the GitHub repository and get IPython Notebook running. See How to use this cookbook."

sent_list = sent_tokenize(para)

# print(sent)

List_of_word_sent = []

for sent in sent_list:
    temp_list = word_tokenize(sent)
    List_of_word_sent.append(temp_list)

for i in List_of_word_sent:
    print(i)

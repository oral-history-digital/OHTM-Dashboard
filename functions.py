import pandas as pd
import json

def top_words(topic, top_dic):
    if type(top_dic) is not dict:
        top_dic = json.loads(top_dic)
    else:
        top_dic = top_dic
    word_dic = {}
    for top_words in top_dic["words"]:
        out_line = []
        for i in range(50):
            out_line.append((top_dic["words"][top_words])[i][1])
        word_dic[top_words] = out_line


    word_dic2 = {}
    for entry in word_dic:
        line = ""
        for out in word_dic[entry]:
            line += out + ", "
        word_dic2[entry] = line
    df1 = pd.DataFrame.from_dict(word_dic2, orient='index')
    df2 = df1.loc[str(topic)]
    return df2
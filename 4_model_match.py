#测试训练好的模型

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告
import sys  
import gensim


if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('wiki.zh.text.model')

    word = model.wv.most_similar(u"足球")
    for t in word:
        print(t[0],t[1])

    '''
    word = model.most_similar(positive=[u'皇上',u'国王'],negative=[u'皇后'])
    for t in word:
        print t[0],t[1]


    print model.doesnt_match(u'太后 妃子 贵人 贵妃 才人'.split())
    print model.similarity(u'书籍',u'书本')
    print model.similarity(u'逛街',u'书本')
    '''

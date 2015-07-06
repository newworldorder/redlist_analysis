import matplotlib.pyplot as plt
from scipy.misc import imread  
from wordcloud import WordCloud, STOPWORDS

if __name__ == '__main__':
    filename = 'data/tidy_redlist.csv'
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    responses = [line.split('|')[1] for line in lines]
    text = ' '.join(responses)
    STOPWORDS.add('security')  # 'security' is uninformative 
    # image source: http://www.stencilry.org/stencils/zombies/zombie-1.gif
    zombie_mask = imread('data/zombie.jpg')
    wc = WordCloud(mask = zombie_mask, stopwords=STOPWORDS).generate(text)

    # show the word cloud 
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

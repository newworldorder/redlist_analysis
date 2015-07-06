import matplotlib.pyplot as plt
from scipy.misc import imread  
from wordcloud import WordCloud

if __name__ == '__main__':
    filename = 'data/tidy_redlist.csv'
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    responses = [line.split('|')[1] for line in lines]
    text = ' '.join(responses)
    text = text.lower()
    text = text.replace('security', '')  # because 'security' is uninformative
    # image pulled from: http://www.stencilry.org/stencils/zombies/zombie-1.gif
    zombie_mask = imread('data/zombie.jpg')
    wc = WordCloud(mask = zombie_mask).generate(text)

    # show the word cloud 
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

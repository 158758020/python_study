import jieba
import wordcloud
import imageio

mask = imageio.imread("素材/心形图片.jpg")
f = open("素材/中国乡村振兴战略.txt","rb")
t = f.read()
f.close()
txt = (" ").join(jieba.lcut(t))

w = wordcloud.WordCloud(width = 1000,\
                        height = 700, font_path = "msyh.ttc",\
                        background_color = "white", mask = mask)
w.generate(txt)
w.to_file("素材/词云图片.png")

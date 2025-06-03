from wordcloud import WordCloud
import matplotlib.pyplot as pyplot

file = open("C:/Users/tjsan/OneDrive/바탕 화면/방통대 과제/데이터정보처리입문/노무현대통령님_취임사.txt", "r", encoding="utf-8")

text = file.read()

word_colud = WordCloud(font_path="C:/Users/tjsan/AppData/Local/Microsoft/Windows/Fonts/Pretendard-Regular.otf").generate(text)

pyplot.imshow(word_colud, interpolation="bilinear")
pyplot.show()
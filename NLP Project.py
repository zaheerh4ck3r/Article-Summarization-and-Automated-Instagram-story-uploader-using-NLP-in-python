#Download && parse article and also generate images
print("Welcome to Zaheer's AI/NLP project.")
import requests
from newspaper import Article
import random
url=input("Enter the URL of the article : ")
article=Article(url)
article.download()
article.parse()
xx=list(article.images)
image_url=random.choice(xx)


question=input("1-Use Images within the article. /n2.I am going to give the URL of HD Image?")
if question=='1'.lower():
	image_url=random.choice(xx)
else:
	image_url=input("Give me the URL : ")





#Creating the summary
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
LANGUAGE="english"
SENTENCES_COUNT=1

parser=PlaintextParser.from_string(article.text, Tokenizer(LANGUAGE))
stemmer=Stemmer(LANGUAGE)
summarizer=Summarizer(stemmer)


for sentence in summarizer(parser.document, SENTENCES_COUNT):
	y=str(sentence)

type(y)


#Dowload and save the image
from wand.image import Image


image_blob = requests.get(image_url)
with Image(blob=image_blob.content) as img:
	size=img.size
	print(size)
	print("Use an image with a greater size.")
	img.save(filename="pic.jpg")



#Image_coordinates
width=size[0]
height=size[1]
aspect=width / height
#Ideal coordinates
dims=(1080,1920)
ideal_width=dims[0]
ideal_height=dims[1]
ideal_aspect=ideal_width / ideal_height




#Cropping Image
#Importing Image class from PIL module
from PIL import Image
im = Image.open(r"pic.jpg")

left=0
top=0
right=ideal_aspect*height
bottom=height
im1 = im.crop((left, top, right, bottom))
newsize = (1920,1080)
im2 = im.resize(newsize)
im2.show()
im2.save('cropped_1.jpg')


from wand.image import Image
from wand.color import Color
from wand.font import Font
with Image(filename='cropped_1.jpg') as canvas:
	canvas.font=Font("bold.otf", size=40)
#	canvas.font=Font("bold.otf",size=13)
	canvas.fill_color=Color("white")
#	caption_width = int(canvas.width/1.2)
#	margin_left = int((canvas.width-caption_width)/2)
#	margin_top = int(canvas.height/2)
	canvas.caption(y,0,200,gravity="center")
#	canvas.caption(y,gravity="center",width=caption_width,left=margin_left,top=margin_top)
	canvas.format='jpg'
	canvas.save(filename='text_overlayed_1.jpg')



#Uploading Image on instagram
from instabot import Bot


bot = Bot()

bot.login(username = input("Enter your username : "),
                password = input("Enter your password : "))

bot.upload_photo("text_overlayed_1.jpg",
                                caption ="This program is made by ZAHEER.")



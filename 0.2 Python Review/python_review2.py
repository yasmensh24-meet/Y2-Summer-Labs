def createytvideo(title,description):
	yt={
	"Title":title,
	"Description":description,
	"Likes":0,
	"Dislikes":0,
	"comments":{}


	}


	return yt



Description=input("give me a description")
Title=input("give me a title")

youtube = createytvideo(Title,Description)

def like(youtube):
	for i in range (495):
		if "Likes" in youtube:
			youtube["Likes"]+=1

	return youtube
y1=like(youtube)
print(y1)

def dislike(youtube):
	if "Dislikes" in youtube:
		youtube["Dislikes"]+=1

	return youtube
y2=dislike(youtube)
print(y2)

comment=input("enter a comment")
username  = input("enter your name")

def addcomment(youtube,username,comment):
	youtube["comments"][username]=comment
	return youtube

y3=addcomment(youtube,username,comment)
print(y3)
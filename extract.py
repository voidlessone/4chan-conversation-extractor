import urllib.request, json 
from bs4 import BeautifulSoup
import re

BOARD = "g"
THREAD = 99559969
with urllib.request.urlopen("https://a.4cdn.org/"+BOARD+"/thread/"+str(THREAD)+".json") as url:
	data = json.load(url)
    
	for post in data["posts"]:
		if "com" in post.keys():
			post["com"] = post["com"].replace("<br>", "\n")
			soup = BeautifulSoup(post["com"], "html.parser")
			post["com"] = soup.get_text()
			reply_to = re.findall(">>(0|[1-9][0-9]*)", post["com"])
			for reply_post in data["posts"]:
				if not "reply_posts" in reply_post.keys():
						reply_post["reply_posts"] = []
				if str(reply_post["no"]) in reply_to:
					
					reply_post["reply_posts"].append(post)
	
	conversations = []
	for post in data["posts"]:
		conversation = []
		if (len(post["reply_posts"])) > 0:
			if "com" in post.keys():
				conversation.append(post["com"])
			else:
				conversation.append("")
				
			for reply in post["reply_posts"]:
				if "com" in reply.keys():
					conversation.append(reply["com"])
		conversations.append(conversation)
		
	print(conversations)
							
									

    

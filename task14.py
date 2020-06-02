  
import json
from pprint import  pprint
with open ("scrape13.json") as scrape:
	a=json.load(scrape)
count=1
co_actors={}
CAST=[]
main_list=[]
for k in a:
	im=k["cast"]
	for j in range(len(im)):
		l=(im[j])
		CAST.append(l)
# print(CAST)?
		# print(l)
		if l['imdb_id'] not in co_actors:
			co_actors[l['imdb_id']]={"name":l["name"],"frequent_co_actors":[]}
			k={}
			if j<len(im)-1:
				h=im[j+1]
				
				k["imdb_id"]=h["imdb_id"]
				k["name"]=h["name"]
				k["num_movies"]=0
				co_actors[l['imdb_id']]["frequent_co_actors"].append(k)
			else:
				pass
		main_list.append(co_actors)
		# main_list.append("1111112222222222222233333333333333333333333333333333111111111111111111111133333333333333333333333333333333333333333333333333333333333333333333")
# for m in co_actors:
# 	for sk in range(len(CAST)-1):
# 		if m==CAST[sk]["imdb_id"]:
# 			if len(co_actors[m]["frequent_co_actors"])!=0:
# 				if co_actors[m]["frequent_co_actors"][0]["imdb_id"]==CAST[sk+1]["imdb_id"]:
# 					co_actors[m]["frequent_co_actors"][0]["num_movies"]+=1
# # with open("scrape14.json","w") as scrape14:
# 	# json.dump(co_actors,scrape14,indent=4)

	
# print(co_actors)
print(main_list)



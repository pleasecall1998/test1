#text="马作的卢飞快，\n弓如霹雳玄晶，\n了却君王天下事，\n赢得生前身后名，\n可怜白发生"
#f1=open("my_file.txt","a")
#f1.write(text)
#f1.close()
f2=open("my_file.txt","r")
#content=f2.readline()
#content2=f2.readline()
content=f2.readlines()
print(content)

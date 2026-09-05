#program to find whether a given post is talking about zarish or not

post = input ("Enter the post: ")

if("Zarish".lower() in post.lower()):
    print("this post is talking about zarish")
    
else:
    print("this post isn't talking about zarish")
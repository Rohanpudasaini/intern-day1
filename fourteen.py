# 14. Write a Python function to create the HTML string with tags around the 
# word(s). 
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>' 
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>' 

def add_tag(tag:str, string:str) ->str:
    return f"<{tag}>{string}</{tag}>"

print(add_tag("h1", "Rohan"))
jose = "My name is Jose"
wds = jose.split()
print(wds)
jose = "user1;user2;user3"
wds = jose.split(';')
print(wds)
wds = ["this','is,'a','sentence"]
glue = '""'
s = glue.join(wds)
print(s)


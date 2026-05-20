#list compr

users=[{"name":"Nara","active":True},
       {"name":"leela","active":True},
       {"name":"subbu","active":False},
       {"name":"lsli","active":True},
       {"name":"vathi","active":True},
       ]

active_users=[user["name"] for user in users if user["active"]]

print(active_users)
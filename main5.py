# friends={"Sabyrzhan" : "Germany", "Zhasulan" : "Qyzylorda", "Mustafa" : "Almaty"}

# for i , x in friends.items():
#     print('Name: ', i, "\nCity: ", x)

friends_names= ["Katya", "Lesha", "David", "Lena"]
friends_cities= ["Astana", "Kokshetau", "Taraz", "Almaty"]
friends={}
for i in range(len(friends_names)):
    friends[i]=friends_names[i]+" "+"lives in" +" "+friends_cities[i]
print(friends[0])
list_following = []
list_followers = []

# imports the following file and when profile picture is found the
# next line is the username at that username is saved to a list.
with open("following.txt", "r") as f:
    line = f.readline()
    while line != "":
        if "profile picture" in line:
            line = f.readline()
            list_following.append(line.replace("\n", ""))
        line = f.readline()

with open("followers.txt", "r") as f:
    line = f.readline()
    while line != "":
        if "profile picture" in line:
            line = f.readline()
            list_followers.append(line.replace("\n", ""))
        line = f.readline()

mutual = []

# for the list of follower if the value is also in following save in
# mutual list and remove from both follower and following lists
for i in list_followers:
    if i in list_following:
        # print(i)
        mutual.append(i)
        list_following.remove(i)

for i in mutual:
    if i in list_followers:
        list_followers.remove(i)

mutual.sort()
list_followers.sort()
list_following.sort()

print("Mutual")
print(mutual)
print()
print("Not following back")
print(list_followers)
print()
print("Doesn't follow back")
print(list_following)
print()

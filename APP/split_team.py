team_members = ""
member = []
for i in range(5):
    team_members+=input()+"\n"

team_members = team_members.split("\n")
for i in team_members:
    team_member = i.rstrip(" joined the lobby")
    member.append(team_member)

for i in member:
    print(i)


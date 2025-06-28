#WAP to detect tghe double space in a  string and replace double space with single space.
s="ram is a  good  boy he  never speak  lie"
print(s.find("   "))
print(s.replace("  " ," ").replace(" ","   "))
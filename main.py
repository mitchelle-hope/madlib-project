# we are creating a game that completes peoples sentences or paragraphs by using string concutination
# we want to create a sring that says "suscribe to.............."
youtuber = " Mitchelle hope's channel"
#different ways to go about concutenation
print("subscribe to" + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adject = input("adjective1:")
adjective2 = input("adjective2:")
celebrity = input("celebrity:")
madlib = f"The experience of making choclate cakes is so {adject}! i cannot stop {adjective2} n\
        this feeling is the most devine feeling ive ever felt, since i became a top{celebrity}! on hells kitchen"
print(madlib)

word = input("words:")
worda = input("worda:")

problems =f" i  have had a  decided to stay indoors till  the {words}! is over,\n i do not want to travel without a {worda}!\n  i might get infected"
print(problems)
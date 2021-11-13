
class user:
    id: int
    first_name: str
    last_name: str
    icon: str

    def __init__(self, id: int, fname: str, lname: str, icon: str, iconimage: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.icon = icon
        self.iconimage = iconimage

# <img src="static/sports.jpeg"/>

def iconfunction(kris, ramses, gary, bell, kevin) -> list[str]:
    if kris >= ramses and kris >= gary and kris >= bell and kris >= kevin:
        return ["static/kris.jpg", "Congratulations! You are Kris Jordan, a professor in the Computer Science department. You are infamous around campus for a number of things of which include: riding around on your scooter, being one of UNC’s best figure skaters, having an instagram famous dog (shout out ada_dog_omg), and liking computers to a small extent. "]
    if ramses >= kris and ramses >= gary and ramses >= bell and ramses >= kevin:
        return ["static/ramses.jpg", "Ra Ra Carolina, lina. It's a great day to be Ramses. As Ramses you are frequently spotted at all sporting events. You love to cheer on your Tar Heels, nothing could make you happier. While most people think of you as a happy individual you do have a dark side when it comes to your arch nemesis … the Blue Devil. "]
    if gary >= kris and gary >= ramses and gary >= bell and gary >= kevin:
        return ["static/gary.jpg", "….Yay? You are Gary the preacher. You are extremely passionate about your beliefs and love to educate others on them. You can frequently be found holding outdoor philosophy classes on the quad because a normal classroom wouldn't be able to seat the number of students who attend your lectures. When people don’t believe your infamy at UNC you just direct them to your rate my professor page which speaks for itself (https://www.ratemyprofessors.com/ShowRatings.jsp?tid=852570)."]
    if bell >= kris and bell >= ramses and bell >= gary and bell >= kevin:
        return ["static/belltower.jpeg", "Hark the sounds because you are the bell tower. You love Carolina so much you never leave. No matter the time or the day, you never cease to be there for your community. Without you students would be late to all their classes. Thank you for your services bell tower :)"]
    if kevin >= kris and kevin >= ramses and kevin >= gary and kevin >= bell:
        return ["static/kevin.jpeg", "Aye it Kevin G. No no no, not Kevin G from Mean Girls. The one and only Kevin G chancellor. Of The University of North Carolina at Chapel Hill. Your day to day life consists of hanging out in the South Building and E-signing emails."]
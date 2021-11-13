from flask import Flask, render_template
from flask import Flask, render_template, request
from helpers import user, iconfunction

app: Flask = Flask(__name__)
users: list[user] = []
user_number: int = 0


kris: int = 0
ramses: int = 0
gary: int = 0
bell: int = 0
kevin: int = 0

def icon_reset() -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    kris = 0
    ramses = 0
    gary = 0
    bell = 0
    kevin = 0


def q1(major: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if major == "stem":
        kris += 1
        bell += 1
    elif major == "soc":
        kevin += 1
        ramses += 1
    elif major == "hum":
        gary += 1


def q2(star: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if star == "air":
        kevin += 1
    elif star == "wat":
        ramses += 1
    elif star == "ear":
        kris += 1
        bell += 1
    elif star == "fire":
        gary += 1


def q3(media: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if media == "youtube":
        kris += 1
    elif media == "instagram":
        ramses += 1
        bell += 1
    elif media == "snapchat":
        ramses += 1
    elif media == "twitter":
        gary += 1
    elif media == "facebook":
        kevin += 1


def q4(transport: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if transport == "car":
        kevin += 1
    elif transport == "bus":
        ramses += 1
    elif transport == "walk":
        gary += 1
        ramses += 1
    elif transport == "scooter":
        kris += 1
    elif transport == "plane":
        gary += 1
    elif transport == "train":
        kevin += 1
        gary += 1


def q5(image: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if image == "imga":
        ramses += 1
    elif image == "imgb":
        gary += 1
        bell += 1
    elif image == "imgc":
        kris += 1
        kevin += 1
    elif image == "imgd":
        kevin += 1


def q6(trad: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if trad == "rush":
        ramses += 1
    elif trad == "hack":
        kris += 1
    elif trad == "well":
        kevin += 1
        ramses += 1
        bell += 1
    elif trad == "library":
        gary += 1


def q7(building: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if building == "bell":
        bell += 1
    elif building == "well":
        kevin += 1
    elif building == "quad":
        gary += 1
    elif building == "davis":
        kris += 1
    elif building == "dean":
        ramses += 1


def q8(comp: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if comp == "comment":
        gary += 1
    elif comp == "dict":
        ramses += 1
        bell += 1
    elif comp == "note":
        kris += 1
    elif comp == "unit":
        kevin += 1


def q9(coach: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if coach == "roy":
        ramses += 1
    elif coach == "dean":
        ramses += 1
        bell += 1
    elif coach == "mack":
        kevin += 1
        ramses += 1
    elif coach == "anson":
        ramses += 1
    elif coach == "god":
        gary += 1
    elif coach == "kris":
        kris += 1


def q10(cheer: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if cheer == "ded":
        ramses += 1
        kevin += 1
        bell += 1
    elif cheer == "comp":
        kris += 1
    elif cheer == "preach":
        gary += 1
    elif cheer == "smart":
        kevin += 1
        kris += 1


def q11(slang: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if slang == "formal":
        kevin += 1
        gary += 1
    elif slang == "hj":
        kris += 1
        bell += 1
    elif slang == "home":
        ramses += 1


def q12(history: str) -> None:
    global kris
    global ramses
    global gary
    global bell
    global kevin
    if history == "bball":
        ramses += 1
    elif history == "heavens":
        gary += 1
        bell += 1
    elif history == "unc":
        kevin += 1
        kris += 1
    elif history == "blue":
        kevin += 1


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        major: str = request.form['major']
        star: str = request.form['star']
        media: str = request.form['media']
        image: str = request.form['image']
        trad: str = request.form['trad']
        building: str = request.form['building']
        comp: str = request.form['comp']
        coach: str = request.form['coach']
        cheer: str = request.form['cheer']
        slang: str = request.form['slang']
        history: str = request.form['history']
        transport: str = request.form['transport']


        if fname == '' or lname == '':
            return render_template("quiz.html")

        question_1: str = q1(major)
        question_2: str = q2(star)
        question_3: str = q3(media)
        question_4: str = q4(transport)
        question_5: str = q5(image)
        question_6: str = q6(trad)
        question_7: str = q7(building)
        question_8: str = q8(comp)
        question_9: str = q9(coach)
        question_10: str = q10(cheer)
        question_11: str = q11(slang)
        question_12: str = q12(history)
        print(kris)
        print(ramses)
        print(gary)
        print(bell)
        print(kevin)


        iconlist: list[str] = iconfunction(kris, ramses, gary, bell, kevin)
        icon: str = iconlist[1]
        iconimage: str = iconlist[0]

        icon_reset()
        new_user: user = user(user_number, fname, lname, icon, iconimage)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", icon=icon, iconimage=iconimage)
    return render_template("quiz.html")


@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])


@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)

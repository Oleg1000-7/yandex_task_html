from flask import Flask, render_template, url_for, redirect

from forms.login_form import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)


@app.route("/list_prof/<list>")
def list_prof(list):
    profs = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
             "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
             "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    return render_template("list_prof.html", list=list, profs=profs)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    answers = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template("answer.html", answers=answers, title=answers["title"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "Форма отправлена"
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

questions_SS = [
    "Have you experienced depressive mood? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
    "Have you experienced loss of interest or pleasure? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
    "Have you experienced loss of energy? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: "
]
questions_MS = [
    "Have you experienced loss of confidence or self-esteem? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
    "Have you experienced unreasonable feelings of self-reproach or inappropriate guilt? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
    "Have you had any thoughts of death or suicide? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
    "Have you experienced diminished ability to think, concentrate or indecisiveness? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
    "Have you experienced sleep disturbance? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
    "Have you experienced change in appetite with weight change? \n a)No never \n b)Maybe a few times \n c)Yes, recently in the past two weeks \n d)Yes, recurrently\nAnswer: ",
]



from flask import Flask
from flask import render_template, request

from health import Health
import json

app = Flask(__name__)

health = Health(json.load(open('data.json')))

@app.route("/")
def index():
    health.reset()
    questions = health.generate_question()
    return render_template('form.html', questions=questions)

@app.route("/results", methods=['GET', 'POST'])
def results():
    if health.results == {}:
        for i in request.form.items():
            health.save_answer(i[0], i[1])
    health.evaluate()
    return render_template('results.html', results=health.results)


"""SS = 0
MS = 0
score = 0



if SS > 3:
    flag_SS = True
    print("Patient presents core symptoms")
if MS > 5:
    flag_MS = True

elif SS == 3:
    flag_SS = False
elif SS < 3:"""



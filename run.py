import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


'''
The angle brackets will pass in data from the URL path, into our view below, and I've
opted to call this parameter: member_name
'''
@app.route("/about/<member_name>")

def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data= json.load(json_data)
        '''
        Next, we will iterate through that data array that we've just created.
        I will just give the variable name of 'obj', which is just an abbreviation for 'object'.
        '''
        for obj in data:
            '''
            Then we want to check if that object's url key from the file, is equal to the member_name
            we've passed through from the URL path.
            '''
            if obj["url"] == member_name:
                '''
                If they do match, then we want our empty 'member'
                '''
                member = obj
    '''
    Instead of returning hard-coded HTML, I will "return render_template".
    The first argument is going to be our new "member.html" template that we just created.
    The second argument will be 'member=member'
    This first 'member' is the variable name being passed through into our html file.
    The second 'member' is the member object we created above on line 24.
    '''
    return render_template("member.html", member=member)
    '''
    return "<h1>" + member["name"] + "</h1>"
    Just to demonstrate that, we are going to return some HTML, the same as we did in one
    of our earlier videos.
    For now, I will just return "<h1>" + member["name"] + "</h1>".
    '''


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have recived your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact") 


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
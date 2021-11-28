from flask import Blueprint, render_template

# Roots files
views = Blueprint(__name__, "views")

@views.route("/soupIMDb")
def home():    
    return render_template("imdbindex.html")




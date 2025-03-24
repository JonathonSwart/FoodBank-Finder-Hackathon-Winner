from flask import render_template, request, session, redirect, url_for
from FoodBankFinder import app
from FoodBankFinder import nearby_banks


@app.route('/', methods=["POST", "GET"])
def home():
    """
    Displays the foodbank finder website
    """
    if request.method == "POST":
        session['pc'] = request.form['postal_code']
        session['rad'] = request.form['radius']
        return redirect(url_for('results'))
    else:
        return render_template('home.html')


@app.route('/results')
def results():
    postal_code = session['pc']
    radius = session['rad']
    banks = nearby_banks.get_banks(postal_code, radius)
    highest, closest = nearby_banks.find_highlights(banks)
    return render_template('results.html', highest=highest, closest=closest, banks=banks)

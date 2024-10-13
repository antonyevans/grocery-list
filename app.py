from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery.db'
db = SQLAlchemy(app)

class GroceryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    checked_date = db.Column(db.DateTime, nullable=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item_name = request.form['item_name']
        new_item = GroceryItem(name=item_name)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))

    one_week_ago = datetime.utcnow() - timedelta(days=7)
    items = GroceryItem.query.filter(
        (GroceryItem.is_active == True) | 
        ((GroceryItem.is_active == False) & (GroceryItem.checked_date > one_week_ago))
    ).order_by(GroceryItem.is_active.desc(), GroceryItem.date_added.desc()).all()
    
    return render_template('index.html', items=items)

@app.route('/toggle/<int:id>')
def toggle_item(id):
    item = GroceryItem.query.get_or_404(id)
    item.is_active = not item.is_active
    if not item.is_active:
        item.checked_date = datetime.utcnow()
    else:
        item.checked_date = None
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

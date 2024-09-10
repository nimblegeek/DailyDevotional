from flask import Flask, render_template, jsonify
from database import get_db_connection, init_db
import random

app = Flask(__name__)

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/devotional/<mood>')
def get_devotional(mood):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Get a random quote and prayer for the given mood
    cur.execute("SELECT quote, prayer FROM devotionals WHERE mood = %s ORDER BY RANDOM() LIMIT 1", (mood,))
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    
    if result:
        return jsonify({
            'quote': result[0],
            'prayer': result[1]
        })
    else:
        return jsonify({
            'quote': "We couldn't find a specific quote for your mood, but remember: God loves you!",
            'prayer': "Dear God, please guide me through this moment and help me find peace."
        }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

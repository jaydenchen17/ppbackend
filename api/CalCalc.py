from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)''')
conn.commit()

# Close the database connection when the application is done
conn.close()

@app.route('/store', methods=['POST'])
def store_data():
    try:
        data = request.get_json()
        value = data['value']

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO data (value) VALUES (?)', (value,))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Data stored successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/retrieve', methods=['GET'])
def retrieve_data():
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM data')
        data = cursor.fetchall()
        conn.close()

        data_list = [{'id': item[0], 'value': item[1]} for item in data]
        return jsonify(data_list)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
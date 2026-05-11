from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return 'OK', 200

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        port=int(os.getenv('DB_PORT', 5432)),
        database=os.getenv('DB_NAME', 'gym_pro'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'CoolPass321')
    )


@app.route('/api/db-healthcheck', methods=['GET'])
def db_healthcheck():
    # Open postgres connection and check if it's alive
    try:
        conn = get_db_connection()
        conn.close()
        return 'DB is up', 200
    except psycopg2.Error as e:
        return 'DB is down: ' + str(e), 500
    
@app.route('/api/get-user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Users WHERE id = %s', (user_id,))

@app.route('/api/get-license-plate/<int:user_id>', methods=['GET'])
def get_licenseplate(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT Parking."User ID" FROM Parking WHERE id = %s', (user_id))
    
    # Jsonify the result and return it
    user = cur.fetchone()
    if user:
        cur.execute('SELECT * FROM Users WHERE id = %s', (user,))
        return 
    else:
        return 'User not found', 404
    
    cur.close()
    conn.close()
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5431)
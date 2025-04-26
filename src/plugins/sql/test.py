from flask import Flask, jsonify
import MySQLdb
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    try:
        # Fetch MySQL connection details from environment variables
        connection = MySQLdb.connect(
            host="localhost",
            port=int("3307"),
            user="root",
            passwd="*2fKh9ljTJNk6iyj1Txl0e&*15&^%%Kwwm%^j6OwbvM4AfRw6S",
            db="jarvis-system"
        )
        connection.ping()  # Optional: Check connection is alive
        connection.close()
        return jsonify(status="online"), 200
    except MySQLdb.Error as e:
        print(f"MySQL Error: {e}")
        return jsonify(status="offline"), 503



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=28042)
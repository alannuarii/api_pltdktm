import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# AWS 
conn = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        port = os.getenv('DB_PORT'),
        user = os.getenv('DB_USER'), 
        password = os.getenv('DB_PASSWORD'),
        db = os.getenv('DB_NAME'),  
        )

cur = conn.cursor(dictionary=True)
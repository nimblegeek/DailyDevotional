import os
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['PGHOST'],
        database=os.environ['PGDATABASE'],
        user=os.environ['PGUSER'],
        password=os.environ['PGPASSWORD'],
        port=os.environ['PGPORT']
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Create table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS devotionals (
            id SERIAL PRIMARY KEY,
            mood VARCHAR(50) NOT NULL,
            quote TEXT NOT NULL,
            prayer TEXT NOT NULL
        )
    ''')
    
    # Insert sample data if the table is empty
    cur.execute("SELECT COUNT(*) FROM devotionals")
    if cur.fetchone()[0] == 0:
        sample_data = [
            ('happy', 'Rejoice in the Lord always. I will say it again: Rejoice! - Philippians 4:4', 'Thank you, Lord, for the joy in my heart. Help me spread this happiness to others.'),
            ('sad', 'The Lord is close to the brokenhearted and saves those who are crushed in spirit. - Psalm 34:18', 'Heavenly Father, comfort me in my sadness and remind me of your endless love.'),
            ('anxious', 'Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. - Philippians 4:6', 'Dear God, calm my anxious thoughts and fill me with your peace that surpasses all understanding.'),
            ('grateful', 'Give thanks to the Lord, for he is good; his love endures forever. - Psalm 107:1', 'Lord, I am grateful for all the blessings in my life. Thank you for your endless love and grace.'),
            ('angry', 'A gentle answer turns away wrath, but a harsh word stirs up anger. - Proverbs 15:1', 'God, help me to let go of my anger and respond with kindness and understanding.'),
        ]
        cur.executemany("INSERT INTO devotionals (mood, quote, prayer) VALUES (%s, %s, %s)", sample_data)
    
    conn.commit()
    cur.close()
    conn.close()

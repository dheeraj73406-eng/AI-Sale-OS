import sqlite3

def add_column(cursor, table, column, type_="VARCHAR"):
    try:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {type_}")
        print(f"Added {column} to {table}")
    except sqlite3.OperationalError as e:
        print(f"Skipped {column} for {table}: {e}")

conn = sqlite3.connect('ai_sales_os.db')
c = conn.cursor()

add_column(c, 'admins', 'business_address')
add_column(c, 'admins', 'profile_photo')

add_column(c, 'settings', 'business_description')
add_column(c, 'settings', 'business_address')
add_column(c, 'settings', 'business_phone')
add_column(c, 'settings', 'business_email')
add_column(c, 'settings', 'website_url')
add_column(c, 'settings', 'social_media_links')
add_column(c, 'settings', 'working_hours')
add_column(c, 'settings', 'business_logo')

conn.commit()
conn.close()

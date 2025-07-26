import sqlite3

def find_scheme(keywords, language):
    conn = sqlite3.connect('db/schemes.db')
    c = conn.cursor()
    # Try to find a scheme matching any keyword and language
    for kw in keywords:
        c.execute('''SELECT name, eligibility, documents, steps, contact, video_url, apply_links FROM schemes WHERE language=? AND keywords LIKE ? LIMIT 1''', (language, f'%{kw}%'))
        row = c.fetchone()
        if row:
            conn.close()
            return {
                'name': row[0],
                'eligibility': row[1],
                'documents': row[2],
                'steps': row[3],
                'contact': row[4],
                'video_url': row[5],
                'apply_links': row[6],
            }
    # Fallback: try all languages
    for kw in keywords:
        c.execute('''SELECT name, eligibility, documents, steps, contact, video_url, apply_links FROM schemes WHERE keywords LIKE ? LIMIT 1''', (f'%{kw}%',))
        row = c.fetchone()
        if row:
            conn.close()
            return {
                'name': row[0],
                'eligibility': row[1],
                'documents': row[2],
                'steps': row[3],
                'contact': row[4],
                'video_url': row[5],
                'apply_links': row[6],
            }
    conn.close()
    return None 
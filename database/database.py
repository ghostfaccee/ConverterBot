import sqlite3
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class Database:

    def __init__(self, db_path: str = 'sqlite3.db'):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    language TEXT NOT NULL DEFAULT 'en',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            logger.info(f'Database {self.db_path} initialized successfully')

    @contextmanager
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row # To obtain results in dictionary format
        try:
            yield conn
        except Exception as e:
            conn.rollback()
            logger.error(f'Database {self.db_path} error: {e}')
            raise
        finally:
            conn.close()
    
    def get_user_language(self, user_id: int) -> str:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT language FROM users WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            if result:
                return result['language']
            else:
                self.create_user(user_id)
                return 'en'
    
    def create_user(self, user_id: int, language: str = 'en'):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT OR REPLACE INTO users (user_id, language) VALUES (?, ?)', (user_id, language,))
            conn.commit()
            logger.info(f'User {user_id} created with language {language}')
    
    def update_user_language(self, user_id: int, language: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET language = ? WHERE user_id = ?', (language, user_id,))
            conn.commit()
            logger.info(f'User {user_id} language updated to {language}')

db = Database()

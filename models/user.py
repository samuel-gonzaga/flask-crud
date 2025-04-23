# from werkzeug.security import generate_password_hash, check_password_hash
# from database.db import Database

# class User:
#     def __init__(self, username, password_hash=None):
#         self.username = username
#         self.password_hash = password_hash

#     @classmethod
#     def create(cls, username, password):
#         password_hash = generate_password_hash(password)  # Gera o hash
#         db = Database()
#         db.cursor.execute(
#             'INSERT INTO users (username, password_hash) VALUES (%s, %s) RETURNING id',
#             (username, password_hash)
#         )
#         user_id = db.cursor.fetchone()[0]
#         db.conn.commit()
#         return cls(username, password_hash)

#     @classmethod
#     def get_by_username(cls, username):
#         db = Database()
#         db.cursor.execute(
#             'SELECT username, password_hash FROM users WHERE username = %s',
#             (username,)
#         )
#         user_data = db.cursor.fetchone()
#         if user_data:
#             return cls(user_data[0], user_data[1])
#         return None

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)  # Verifica o hash
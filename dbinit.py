from scheduler import db
"""
    create test database
"""
if __name__ == "__main__":
	db.drop_all()
    db.create_all()

from db import SessionLocal
from models import Episode

db = SessionLocal()
try:
    deleted = db.query(Episode).delete()
    db.commit()
    print(f"✅ Deleted {deleted} episodes.")
except Exception as e:
    db.rollback()
    print("❌ Error:", e)
finally:
    db.close()
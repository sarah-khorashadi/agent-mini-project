from datetime import datetime, timedelta

from app.core.database import SessionLocal
from app.models.user import User


def seed_users():
    db = SessionLocal()

    try:
        mock_users = [
            User(
                user_id=1,
                name="Alice",
                segment="new_user",
                created_at=datetime.utcnow() - timedelta(days=10),
                last_seen_at=datetime.utcnow() - timedelta(days=1),
            ),
            User(
                user_id=2,
                name="Bob",
                segment="active_user",
                created_at=datetime.utcnow() - timedelta(days=30),
                last_seen_at=datetime.utcnow() - timedelta(hours=5),
            ),
            User(
                user_id=3,
                name="Charlie",
                segment="at_risk_user",
                created_at=datetime.utcnow() - timedelta(days=60),
                last_seen_at=datetime.utcnow() - timedelta(days=20),
            ),
        ]

        # optional: avoid duplicates (simple check)
        existing_ids = {u.user_id for u in db.query(User.user_id).all()}

        new_users = [u for u in mock_users if u.user_id not in existing_ids]

        db.add_all(new_users)
        db.commit()

        print(f"Seeded {len(new_users)} users")

    except Exception as e:
        db.rollback()
        print("Seed error:", e)

    finally:
        db.close()
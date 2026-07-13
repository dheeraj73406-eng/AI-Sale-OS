import os
import sys

# Ensure backend module can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend import database, models, main
from backend.database import SessionLocal

def verify():
    print("Testing V2 SQLite connection and database seeding...")
    db = SessionLocal()
    try:
        # Trigger seeding explicitly for this test
        main.seed_database(db)
        
        # Check tables counts
        cust_count = db.query(models.Customer).count()
        conv_count = db.query(models.Conversation).count()
        msg_count = db.query(models.Message).count()
        
        print(f"Success: Found {cust_count} customers in database.")
        print(f"Success: Found {conv_count} conversations in database.")
        print(f"Success: Found {msg_count} messages in database.")
        
        # Verify relationships and status auto-assignment
        customers = db.query(models.Customer).all()
        hot_leads = 0
        warm_leads = 0
        cold_leads = 0
        
        for c in customers[:5]:
            print(f"- Lead: {c.name} ({c.company or 'No Company'})")
            print(f"  Platform: {c.platform} | Status: {c.lead_status} (Score: {c.lead_score})")
            
            # Relation check
            convs = c.conversations
            print(f"  Conversations associated: {len(convs)}")
            if convs:
                msgs = convs[0].messages
                print(f"  Messages in first conversation: {len(msgs)}")
            
            # Status tallies
            if c.lead_status == "Hot":
                hot_leads += 1
            elif c.lead_status == "Warm":
                warm_leads += 1
            else:
                cold_leads += 1
                
        print(f"Lead status distribution (first 5): Hot: {hot_leads}, Warm: {warm_leads}, Cold: {cold_leads}")
        
        if cust_count >= 15 and conv_count >= 15:
            print("Database has been successfully seeded with 15+ customers and conversations.")
            return True
        else:
            print(f"Warning: Unexpected count in database.")
            return False
            
    except Exception as e:
        print(f"V2 Database verification failed: {e}")
        return False
    finally:
        db.close()

if __name__ == "__main__":
    success = verify()
    sys.exit(0 if success else 1)

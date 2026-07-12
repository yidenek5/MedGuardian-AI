# MedGuardian AI - Database Schema

## 1. Overview

MedGuardian AI uses a relational database structure to store users, medicines, reminders, health records, and medication history.

Database Technology:

SQLite

The database is designed to support:

- Multiple users
- Multiple medicines per user
- Multiple reminders per medicine
- Medication tracking
- Family management
- Health records

---

# 2. Entity Relationship Overview

```
User
 |
 | 1 : Many
 |
Medicine
 |
 | 1 : Many
 |
Reminder
 |
 | 1 : Many
 |
Medicine History


User
 |
 | 1 : Many
 |
Journal Entry


User
 |
 | 1 : Many
 |
Family Member
```

---

# 3. Users Table

Stores application user information.

Table:

```
users
```

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| name | TEXT | User full name |
| email | TEXT | User email |
| password_hash | TEXT | Encrypted password |
| created_at | DATETIME | Account creation date |

---

# 4. Medicines Table

Stores medicine information belonging to users.

Table:

```
medicines
```

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| user_id | INTEGER | Owner of medicine |
| name | TEXT | Medicine name |
| dosage | TEXT | Amount per dose |
| medicine_type | TEXT | Tablet, capsule, syrup |
| quantity | INTEGER | Available amount |
| frequency | TEXT | Daily, weekly, interval |
| meal_instruction | TEXT | Before/after food |
| start_date | DATE | Treatment start |
| end_date | DATE | Treatment end |
| notes | TEXT | Additional information |

Relationship:

```
One User → Many Medicines
```

---

# 5. Reminders Table

Stores medicine schedules.

Table:

```
reminders
```

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| medicine_id | INTEGER | Related medicine |
| reminder_time | TIME | Notification time |
| status | TEXT | Pending, completed, missed |
| repeat_type | TEXT | Daily, weekly, interval |

Relationship:

```
One Medicine → Many Reminders
```

Example:

```
Paracetamol

Reminder:
08:00 AM

Reminder:
08:00 PM
```

---

# 6. Medicine History Table

Stores medication activity.

Table:

```
medicine_history
```

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| reminder_id | INTEGER | Related reminder |
| taken_time | DATETIME | Actual action time |
| status | TEXT | Taken, missed, skipped |

Used for:

- Adherence calculation
- Reports
- Analytics

---

# 7. Journal Entries Table

Stores health notes.

Table:

```
journal_entries
```

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| user_id | INTEGER | Owner |
| date | DATE | Entry date |
| symptoms | TEXT | Health symptoms |
| notes | TEXT | User notes |

---

# 8. Family Members Table

Stores people managed by a caregiver.

Table:

```
family_members
```

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Primary key |
| user_id | INTEGER | Caregiver |
| name | TEXT | Member name |
| relationship | TEXT | Parent, child, etc. |

---

# 9. Database Relationships

## User → Medicine

Relationship:

```
One-to-Many
```

Example:

```
Abebe

    Medicine 1:
    Paracetamol

    Medicine 2:
    Vitamin D
```

---

## Medicine → Reminder

Relationship:

```
One-to-Many
```

Example:

```
Amoxicillin

08:00 AM
04:00 PM
12:00 AM
```

---

## Reminder → History

Relationship:

```
One-to-Many
```

Stores:

```
Taken
Missed
Snoozed
```

---

# 10. Data Integrity Rules

The system must ensure:

- Email addresses are unique.
- Medicine names cannot be empty.
- Quantity cannot be negative.
- Reminder time must be valid.
- Every medicine belongs to a user.
- Deleted medicines remove related reminders.

---

# 11. Future Database Expansion

Possible future tables:

```
drug_interactions

notifications

doctor_profiles

ai_recommendations

backup_records
```

---

# 12. Database Design Principles

The database follows:

## Normalization

Avoid duplicate information.

## Data Integrity

Keep data accurate and consistent.

## Scalability

Allow future features without redesigning the database.
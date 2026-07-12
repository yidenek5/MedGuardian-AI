# MedGuardian AI - Software Architecture

## 1. Overview

MedGuardian AI follows a layered software architecture that separates the user interface, business logic, data management, and supporting services.

The architecture improves:

- Maintainability
- Scalability
- Testing
- Code organization
- Future expansion

---

# 2. Architecture Pattern

## Layered Architecture

The system is divided into the following layers:

```
+--------------------------------+
|        Presentation Layer      |
|        (Tkinter GUI)           |
+--------------------------------+
              |
              ↓
+--------------------------------+
|        Service Layer           |
|   (Business Logic Processing)  |
+--------------------------------+
              |
              ↓
+--------------------------------+
|        Core Layer              |
| Database, Security, Scheduler  |
+--------------------------------+
              |
              ↓
+--------------------------------+
|        Data Layer              |
|        SQLite Database         |
+--------------------------------+
```

---

# 3. System Components

## 3.1 Presentation Layer

Location:

```
src/ui/
```

Responsibility:

Provides interaction between users and the system.

Components:

- Login Window
- Registration Window
- Dashboard
- Medicine Management Screens
- Analytics Screens
- Settings

Technology:

- Tkinter

---

## 3.2 Service Layer

Location:

```
src/services/
```

Responsibility:

Contains the application's business logic.

Components:

### Medicine Service

Handles:

- Adding medicines
- Updating medicines
- Removing medicines
- Searching medicines

---

### Reminder Service

Handles:

- Creating schedules
- Managing reminder times
- Tracking reminder status

---

### Notification Service

Handles:

- Desktop notifications
- Alerts
- Warning messages

---

### Analytics Service

Handles:

- Adherence calculation
- Reports
- Statistics

---

## 3.3 Core Layer

Location:

```
src/core/
```

Responsibility:

Provides common system functionality.

Components:

### Database Manager

Handles:

- Database connection
- Queries
- Transactions

---

### Security Manager

Handles:

- Password encryption
- User authentication

---

### Scheduler

Handles:

- Background reminder checking
- Scheduled tasks

---

## 3.4 Data Layer

Location:

```
database/
```

Responsibility:

Stores permanent application data.

Technology:

SQLite

Main tables:

```
Users

Medicines

Reminders

Medicine_History

Journal_Entries

Family_Members
```

---

# 4. Application Data Flow

Example: User adds a medicine

```
User
 |
 ↓
Medicine Window
 |
 ↓
Medicine Service
 |
 ↓
Database Manager
 |
 ↓
SQLite Database
```

---

Example: Medicine Reminder

```
Database
 |
 ↓
Scheduler
 |
 ↓
Reminder Service
 |
 ↓
Notification Service
 |
 ↓
User
```

---

# 5. Main Domain Models

Location:

```
src/models/
```

## User

Represents an application user.

Attributes:

- Name
- Email
- Password
- Medicines

---

## Medicine

Represents a user's medicine.

Attributes:

- Name
- Dosage
- Type
- Quantity
- Frequency
- Start Date
- End Date

---

## Reminder

Represents medicine schedules.

Attributes:

- Medicine
- Time
- Status

---

## Journal Entry

Represents health records.

Attributes:

- Date
- Symptoms
- Notes

---

# 6. Project Directory Mapping

```
medguardian-ai/

src/

├── models/
│   └── Application entities

├── services/
│   └── Business operations

├── core/
│   └── System functionality

├── ui/
│   └── User interface

├── utils/
│   └── Helper functions


database/

└── SQLite data storage


docs/

└── Project documentation
```

---

# 7. Future Expansion

The architecture supports future features:

- AI medication assistant
- Cloud synchronization
- Mobile application
- Doctor dashboard
- Voice reminders
- Wearable device integration

---

# 8. Design Principles

The system follows:

## Separation of Responsibilities

Each component has one clear purpose.

## Modularity

Features are independent and reusable.

## Scalability

New features can be added without rewriting the system.

## Maintainability

Code is organized and easy to update.
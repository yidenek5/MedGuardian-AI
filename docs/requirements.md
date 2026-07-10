# MedGuardian AI - Software Requirements Specification (SRS)

## 1. Project Overview

**MedGuardian AI** is an intelligent medicine management desktop application that helps individuals and families organize medications, receive reminders, track adherence, monitor medicine stock, and maintain health records.

---

# 2. Problem Statement

Many people face problems with:

- Forgetting medicine schedules.
- Taking incorrect doses.
- Losing medicine information.
- Running out of medicine unexpectedly.
- Difficulty monitoring family members' medication.

MedGuardian AI solves these problems by providing a centralized digital medicine management system.

---

# 3. Project Objectives

The system aims to:

- Reduce missed medicine doses.
- Provide accurate medicine scheduling.
- Improve medication organization.
- Help users monitor treatment progress.
- Provide health insights through reports.

---

# 4. Target Users

## Individual Users

People who need reminders for daily medications.

## Elderly Users

Users who require simple medication tracking.

## Caregivers

People managing medicines for family members.

---

# 5. Functional Requirements

## 5.1 User Management

The system shall:

- Allow users to create an account.
- Allow users to log in securely.
- Allow users to update their profile.
- Support multiple family member profiles.

### Measurement

- User registration completes within 5 seconds.
- Login response time is less than 2 seconds.

---

# 5.2 Medicine Management

The system shall allow users to:

- Add a medicine.
- Edit medicine information.
- Delete a medicine.
- View all medicines.

Each medicine shall contain:

- Medicine name.
- Dosage.
- Medicine type.
- Quantity.
- Frequency.
- Reminder schedule.
- Start date.
- End date.
- Food instructions.
- Notes.

### Measurement

- User can add a medicine in less than 1 minute.
- System supports at least 100 medicines per user.

---

# 5.3 Reminder System

The system shall:

- Create medicine reminders.
- Support multiple reminders per medicine.
- Support different schedules:
  - Once daily.
  - Multiple times daily.
  - Every X hours.
  - Weekly.

- Notify users at the scheduled time.

### Measurement

- Reminder accuracy should be within ±1 minute.
- System should support at least 500 scheduled reminders.

---

# 5.4 Medicine Tracking

The system shall allow users to:

- Mark medicine as taken.
- Mark medicine as missed.
- View medicine history.

### Measurement

- Every dose action must be saved immediately.
- Users can view previous records.

---

# 5.5 Inventory Management

The system shall:

- Track medicine quantity.
- Calculate remaining doses.
- Warn users when medicine is low.

### Measurement

Example:

```
Quantity: 5 tablets
Threshold: 5 tablets

System displays:
"Medicine refill required"
```

---

# 5.6 Analytics Dashboard

The system shall provide:

- Daily adherence percentage.
- Weekly reports.
- Monthly reports.
- Missed dose statistics.

### Measurement

Reports should load within 3 seconds.

---

# 5.7 Health Journal

The system shall allow users to:

- Add health notes.
- Record symptoms.
- Track medicine effects.

### Measurement

Users can create and edit unlimited journal entries.

---

# 5.8 Drug Interaction Warning

The system shall:

- Check possible medicine interactions.
- Display warnings.

Example:

```
Warning:
Two medicines may interact.
Consult a healthcare professional.
```

### Measurement

The system checks interactions whenever a new medicine is added.

---

# 6. Non-Functional Requirements

## Performance

- Application startup time: less than 5 seconds.
- Database operations: less than 2 seconds.

## Security

- Passwords must be encrypted.
- User data must be protected.

## Usability

- New users should understand the interface within 5 minutes.
- The application should provide clear messages.

## Reliability

- User data should not be lost after application restart.
- Automatic backup should be supported.

## Maintainability

- Code should follow modular architecture.
- Each component should have a single responsibility.

---

# 7. Technology Requirements

## Programming Language

Python 3.x

## GUI

Tkinter

## Database

SQLite

## Libraries

- Plyer (notifications)
- Matplotlib (analytics)
- APScheduler (scheduling)
- Pytest (testing)

---

# 8. Success Criteria

The project is considered successful when:

 = Users can register and log in.

 = Users can manage medicines.

 = Users receive accurate reminders.

 = Users can track taken and missed doses.

 = Users can view medication reports.

 = Users receive refill warnings.

=  The application runs as a desktop application.
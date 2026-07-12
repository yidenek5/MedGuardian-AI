# MedGuardian AI - Use Cases

## Overview

This document describes how users interact with MedGuardian AI to accomplish specific tasks. Each use case defines the goal, actors, conditions, workflow, exceptions, and expected outcome.

---

# UC-001: Register an Account

## Goal

Allow a new user to create an account.

## Primary Actor

User

## Preconditions

- User has not registered an account.

## Main Flow

1. User opens the application.
2. User selects "Register".
3. User enters:
   - Full Name
   - Email Address
   - Password
4. User clicks "Create Account".
5. System validates the information.
6. System creates the account.
7. System displays a success message.

## Alternative Flows

- Email already exists.
- Required fields are empty.
- Invalid email format.

## Postconditions

- A new user account is created.
- User can log in.

---

# UC-002: Log In

## Goal

Allow a registered user to access the application.

## Primary Actor

User

## Preconditions

- User has a registered account.

## Main Flow

1. User enters email.
2. User enters password.
3. User clicks "Login".
4. System verifies credentials.
5. Dashboard opens.

## Alternative Flows

- Incorrect password.
- Email not found.

## Postconditions

- User accesses the dashboard.

---

# UC-003: Add a Medicine

## Goal

Store medicine information for future reminders.

## Primary Actor

User

## Preconditions

- User is logged in.

## Main Flow

1. User clicks "Add Medicine".
2. User enters:
   - Medicine Name
   - Dosage
   - Medicine Type
   - Quantity
   - Frequency
   - Reminder Schedule
   - Start Date
   - End Date
   - Meal Instruction
   - Notes
3. User saves the medicine.
4. System validates the data.
5. System stores the medicine.
6. System creates reminder schedules.

## Alternative Flows

- Required information is missing.
- Invalid schedule.

## Postconditions

- Medicine is saved successfully.
- Reminder schedule is created.

---

# UC-004: Edit a Medicine

## Goal

Update medicine information.

## Primary Actor

User

## Preconditions

- Medicine already exists.

## Main Flow

1. User selects a medicine.
2. User clicks "Edit".
3. User updates information.
4. User saves changes.
5. System updates the medicine.

## Alternative Flows

- Invalid values entered.

## Postconditions

- Medicine information is updated.

---

# UC-005: Delete a Medicine

## Goal

Remove a medicine from the system.

## Primary Actor

User

## Preconditions

- Medicine exists.

## Main Flow

1. User selects a medicine.
2. User clicks "Delete".
3. System asks for confirmation.
4. User confirms deletion.
5. System removes the medicine and its reminders.

## Alternative Flows

- User cancels deletion.

## Postconditions

- Medicine is deleted.

---

# UC-006: Receive a Medicine Reminder

## Goal

Notify the user when it is time to take medicine.

## Primary Actor

System

## Secondary Actor

User

## Preconditions

- Reminder schedule exists.

## Main Flow

1. System checks the current time.
2. Scheduled reminder is reached.
3. Notification appears.
4. User views reminder.

## Alternative Flows

- Reminder service is unavailable.

## Postconditions

- User is notified.

---

# UC-007: Record Medicine Intake

## Goal

Track whether medicine was taken.

## Primary Actor

User

## Preconditions

- Reminder has been displayed.

## Main Flow

1. User opens the reminder.
2. User selects:
   - Taken
   - Missed
   - Snooze
3. System records the action.
4. Dashboard statistics are updated.

## Alternative Flows

- User closes the reminder without selecting an option.

## Postconditions

- Medicine history is updated.

---

# UC-008: Monitor Medicine Inventory

## Goal

Prevent medicine shortages.

## Primary Actor

System

## Preconditions

- Medicine quantity is tracked.

## Main Flow

1. System updates remaining quantity.
2. System compares quantity with refill threshold.
3. Low-stock notification is generated.

## Alternative Flows

- Quantity information is unavailable.

## Postconditions

- User receives a refill warning.

---

# UC-009: View Analytics

## Goal

Display medication performance.

## Primary Actor

User

## Preconditions

- Medication history exists.

## Main Flow

1. User opens Analytics.
2. System calculates:
   - Taken doses
   - Missed doses
   - Adherence percentage
3. Dashboard displays charts and reports.

## Alternative Flows

- No historical data available.

## Postconditions

- Analytics are displayed.

---

# UC-010: Manage Family Members

## Goal

Allow caregivers to manage medicines for family members.

## Primary Actor

Caregiver

## Preconditions

- Caregiver account exists.

## Main Flow

1. Caregiver adds a family member.
2. Caregiver assigns medicines.
3. System creates separate schedules.
4. Caregiver monitors reminders and reports.

## Alternative Flows

- Duplicate family member.

## Postconditions

- Family member is added successfully.

---

# Use Case Summary

| ID | Use Case | Primary Actor |
|----|----------------------------|---------------|
| UC-001 | Register Account | User |
| UC-002 | Log In | User |
| UC-003 | Add Medicine | User |
| UC-004 | Edit Medicine | User |
| UC-005 | Delete Medicine | User |
| UC-006 | Receive Reminder | System |
| UC-007 | Record Medicine Intake | User |
| UC-008 | Monitor Inventory | System |
| UC-009 | View Analytics | User |
| UC-010 | Manage Family Members | Caregiver |
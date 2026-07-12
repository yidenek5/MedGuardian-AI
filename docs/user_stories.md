# MedGuardian AI - User Stories

## Overview

This document describes the application's features from the user's perspective. Each user story represents a real need that MedGuardian AI should satisfy.

---

# Epic 1: Account Management

## US-001: Register an Account

As a new user,

I want to create an account,

So that I can securely save and manage my personal medication records.

### Acceptance Criteria

- User can register with a name, email, and password.
- Email must be unique.
- Password is securely stored.
- User receives confirmation after successful registration.

---

## US-002: Log In

As a registered user,

I want to log into my account,

So that I can access my medicine information securely.

### Acceptance Criteria

- User enters a valid email and password.
- Invalid credentials display an error message.
- Successful login opens the dashboard.

---

# Epic 2: Medicine Management

## US-003: Add a Medicine

As a user,

I want to add a medicine,

So that I can receive reminders and keep all medicine information in one place.

### Acceptance Criteria

A medicine includes:

- Name
- Dosage
- Medicine type
- Quantity
- Frequency
- Reminder schedule
- Start date
- End date
- Meal instruction
- Notes

The medicine is saved successfully.

---

## US-004: Edit a Medicine

As a user,

I want to edit medicine information,

So that my records always stay accurate.

### Acceptance Criteria

- User can update any medicine field.
- Changes are saved immediately.

---

## US-005: Delete a Medicine

As a user,

I want to remove medicines I no longer take,

So that my medicine list stays organized.

### Acceptance Criteria

- User confirms deletion.
- Medicine is permanently removed.

---

# Epic 3: Reminder Management

## US-006: Receive Medicine Reminders

As a user,

I want to receive reminders,

So that I do not forget to take my medicines.

### Acceptance Criteria

- Reminder appears at the scheduled time.
- Reminder includes medicine name and dosage.
- User can mark the reminder as Taken, Missed, or Snooze.

---

## US-007: Support Multiple Daily Reminders

As a user,

I want to schedule medicines once daily, multiple times daily, weekly, or at custom intervals,

So that every medicine follows the correct treatment schedule.

### Acceptance Criteria

The system supports:

- Once daily
- Twice daily
- Three times daily
- Every X hours
- Weekly schedules

---

# Epic 4: Medicine Tracking

## US-008: Record Medicine Intake

As a user,

I want to record whether I took or missed a medicine,

So that I can monitor my treatment progress.

### Acceptance Criteria

Each reminder can be marked as:

- Taken
- Missed
- Snoozed

The action is stored in the user's history.

---

# Epic 5: Inventory Management

## US-009: Receive Low-Stock Warnings

As a user,

I want to know when my medicine is running low,

So that I can refill it before it runs out.

### Acceptance Criteria

- Remaining quantity is tracked.
- Warning appears when quantity reaches the refill threshold.

---

# Epic 6: Analytics

## US-010: View Medication Reports

As a user,

I want to see my medication history and adherence,

So that I understand how consistently I follow my treatment.

### Acceptance Criteria

The dashboard displays:

- Taken doses
- Missed doses
- Adherence percentage
- Daily report
- Weekly report
- Monthly report

---

# Epic 7: Family Management

## US-011: Manage Family Members

As a caregiver,

I want to manage medicines for my family,

So that I can help them follow their treatment schedules.

### Acceptance Criteria

- User can add family members.
- Each family member has separate medicines.
- Each member has separate reminders.

---

# Epic 8: Health Journal

## US-012: Record Health Notes

As a user,

I want to record symptoms and daily health notes,

So that I can monitor my health during treatment.

### Acceptance Criteria

- User can create journal entries.
- Entries include date and notes.
- Previous entries remain available.

---

# Epic 9: Drug Safety

## US-013: Receive Drug Interaction Warnings

As a user,

I want to be warned about possible medicine interactions,

So that I can take medicines more safely.

### Acceptance Criteria

- System checks medicines when a new medicine is added.
- Potential interactions display a warning.
- Warning does not replace professional medical advice.

---

# Future Enhancements

The following features are planned for future versions:

- AI-powered medication insights
- Voice reminders
- QR code medicine scanning
- Cloud backup and synchronization
- Doctor and pharmacist integration
- Wearable device integration

---

# Definition of Done

A user story is considered complete when:

- All acceptance criteria are satisfied.
- The feature is fully implemented.
- The feature is tested.
- The documentation is updated.
- No critical defects remain.
# Manual Test Cases

These test cases cover the basic functionality of the CRUD Python web application, focusing on user data input, validation, database interaction, and error handling.

---

## 1. Add New User

**Steps:**
1. Open the "Add New User" form.
2. Fill in all required fields with valid data.
3. Submit the form.

**Expected Result:**
- New user data is saved in the SQLite database.
- The new user appears in the user list.

---

## 2. Validate Empty Fields

**Steps:**
1. Open the "Add New User" form.
2. Submit the form without filling any required fields.

**Expected Result:**
- The application displays an error message indicating required fields.
- No data is saved to the database.

---

## 3. Edit Existing User

**Steps:**
1. Select an existing user from the user list.
2. Modify user details (e.g., name or email).
3. Submit the changes.

**Expected Result:**
- The user's data is updated in the database.
- The updated information is displayed in the user list.

---

## 4. Delete User

**Steps:**
1. Select a user to delete.
2. Confirm the deletion action (if prompted).

**Expected Result:**
- The user record is removed from the database.
- The user no longer appears in the list.

---

## 5. Invalid Input Handling

**Steps:**
1. Attempt to submit the form with invalid inputs (e.g., invalid email format, numbers in name fields).
2. Submit the form.

**Expected Result:**
- The application displays relevant error messages.
- Data is not saved to the database.

---

## 6. Database Consistency Check

**Steps:**
1. After each CRUD operation, open the database using DB Browser for SQLite.
2. Verify the data matches the performed actions.

**Expected Result:**
- The database contains accurate and consistent data reflecting all changes.
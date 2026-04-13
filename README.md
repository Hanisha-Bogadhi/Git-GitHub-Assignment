# Git & GitHub + Flask Assignment

## Overview
This assignment demonstrates practical usage of Git and GitHub workflows including branching, merging, conflict resolution, reset, and rebase. A Flask-based project is used to implement frontend and backend features.

---

## Technologies Used
- Python (Flask)
- MongoDB
- Git & GitHub

---

##  Assignment Tasks

---

###  1. Repository Setup & Initial Branching
- Created a new GitHub repository.
- Cloned the repository locally using SSH.
- Created a branch named after username.
- Added Flask project files to this branch.
- Committed and merged changes into the `main` branch.

---

###  2. JSON Update with New Branch
- Created a new branch `<your_name>_new`.
- Updated JSON data used in `/api` route.
- Merged branch into `main`.
- Resolved merge conflicts by accepting incoming changes.
- Committed and pushed updates.

---

### 3. Feature Development with Multiple Branches

#### Branches Created:
- `master_1` → Frontend
- `master_2` → Backend

#### Frontend (master_1):
- Created To-Do page with form fields:
  - Item Name
  - Item Description

#### Backend (master_2):
- Created `/submittodoitem` API route
- Accepts:
  - itemName
  - itemDescription
- Stores data in MongoDB

#### Merge:
- Merged both branches into `main`

---

###  4. Advanced Git Operations

#### Enhancing To-Do Form (master_1):
Added fields with separate commits:
1. Item ID
2. Item UUID
3. Item Hash

---

#### Merging to Main:
- Merged `master_1` into `main`

---

#### Git Reset:
- Used `git reset --soft` to revert `main` to only **Item ID field**
- Re-committed with message:
  - *"Reverted to only Item ID field"*

---

#### Rebasing:
- Rebasing performed using:
  ```bash
  git rebase main
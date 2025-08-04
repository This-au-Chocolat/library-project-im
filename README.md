Library Information Management System

Description

This project is a web-based Library Information Management System developed for the Information Management course at UPY. It allows users to browse, filter, and manage a catalog of books through a modern, user-friendly interface. The system features a visually appealing frontend with a purple-based theme and an admin panel for managing book records.
Technologies used: Python, Flask, MongoDB, HTML, CSS, JavaScript.

Installation
Clone the repository:

```
git clone <repository-url>
cd library-project-im
```

Set up the virtual environment:

```
python3 -m venv libp
source libp/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Configure MongoDB:

- Ensure you have a running MongoDB instance.
- Update the database connection in db.py if needed.

Run the application:

```
python backend/app.py
```

Visit http://127.0.0.1:5000/ in your browser.
Usage
Browse Books:
On the homepage, filter books by language and view details in a responsive card layout.

Admin Panel:
Access /admin to add, update, or delete books using the management interface.

Example commands:

Features
Modern, responsive UI with a purple-based color palette
Browse and filter books by language
Add, update, and delete books via the admin panel
Toast notifications and feedback for admin actions
Accessible and user-friendly design
License
This project is licensed under the MIT License. See the LICENSE file for details.

Credits / Acknowledgments
Developed as a project for the Information Management subject at UPY.
Authors:

Lorena Danae Pérez López
Ángel Rivaldo Canché Chuc
Ricardo Daniel Horta Sánchez

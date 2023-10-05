# InfoBridge - CRM Application

Welcome to the InfoBridge CRM Application! Connecting and managing data while facilitating customer interactions and relationship-building through technology. 
This Customer Relationship Management (CRM) system is built using HTML, Bootstrap, Django, and MySQL. InfoBridge allows you to efficiently manage customer data by adding, updating, and deleting customer records. This README file provides an overview of the application's features, installation instructions, and usage guidelines.

## Features

- **User Authentication:** Secure user registration and login system.
- **Customer Management:** Add, update, and delete customer records.
- **Customer Details:** Store and view customer information, including name and contact details.
- **User-Friendly Interface:** A responsive and user-friendly design for seamless navigation.

## Installation

To run InfoBridge on your local machine, follow these installation steps:

### Prerequisites

- Python (3.6 or higher)
- Django (3.0 or higher)
- MySQL database
- Git (optional)

### Installation Steps

1. Clone the repository (if you haven't already):
   ```bash
   git clone https://github.com/ezeiruemma/infobridge.git
   cd infobridge
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure the database settings:
   - Open the `infobridge/settings.py` file.
   - Update the database configuration to match your MySQL settings (database name, user, password).

6. Apply migrations to create database tables:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser for administrative access:
   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```bash
   python manage.py runserver
   ```

9. Access the CRM application in your web browser at `http://localhost:8000/`.

## Usage

1. Register and log in using your credentials.
2. Access the CRM dashboard to start managing customer records.
3. Use the "Add Customer" button to add new customer information.
4. Click on a customer's record to view or update their details.
5. To delete a customer record, select it and choose the "Delete" option.

## Contributing

Contributions to InfoBridge are welcome! If you'd like to enhance or fix issues in the application, please follow the [contribution guidelines](CONTRIBUTING.md).

---

Enjoy using InfoBridge  to efficiently manage your customer relationships! If you have any questions or encounter issues, please feel free to reach out to me.
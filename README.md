# User Onboarding Flask Project

This Flask project is designed for user onboarding with search functionalities. Users can sign up, log in, and view a list of registered users. The project utilizes Flask, MySQL for database management, and includes basic HTML templates for user interaction.

## Project Structure

The main project files and directories are organized as follows:

- `__pycache__`: Python bytecode cache directory.
- `app.py`: Flask application main file containing route definitions and backend logic.
- `static`: Directory containing static files such as CSS and images.
  - `images`: Subdirectory holding image resources used in the project.
  - `signup.css`: Stylesheet for the signup page.
- `templates`: HTML templates for rendering pages.
  - `login.html`: Login page template.
  - `signup.html`: Signup page template.
  - `users.html`: Template for displaying a list of registered users.
- `user.sql`: SQL script for creating the necessary MySQL database and table.

## Dependencies

The project relies on the following Python packages:

- Flask: Micro web framework for Python.
- Flask-MySQLdb: Flask extension for MySQL integration.

Install the dependencies using the following command:

```bash
pip install Flask Flask-MySQLdb
```

## Database Configuration

Ensure that you have a MySQL server running. Update the MySQL configuration in `app.py`:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bank_employee_mgt'
```

## Running the Project

1. Create the MySQL database and table using `user.sql`.
2. Run the Flask application using the following command:

   ```bash
   python app.py
   ```

3. Access the application in your web browser at `http://localhost:5000`.

## Usage

- **Signup**: Visit `http://localhost:5000/signup` to create a new user account.
- **Login**: Access `http://localhost:5000/login` to log in with your credentials.
- **User List**: After logging in, you can view a list of registered users at `http://localhost:5000/login`.

## Important Notes

- Make sure to configure the MySQL connection details in `app.py`.
- This is a basic project and may require further enhancements for production use.

Feel free to explore and modify the project to suit your needs. If you encounter any issues or have suggestions for improvement, please don't hesitate to reach out.

Happy coding! 🚀
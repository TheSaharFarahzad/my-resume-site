# My Resume Site

## Description
This project is my resume website, providing information about me, the field I work in, my contact information, work experiences, skills, education, and languages I know. You can access my social media profiles by clicking on their icons, and you also have the option to print my resume or save it in different formats (PDF, SVG, PNG, JPG).

## Installation

If you want to set up the project on your local machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/TheSaharFarahzad/my-resume-site.git
   ```

2. **Navigate into the Project Directory:**
   ```bash
   cd my-resume-site
   ```

3. **Create and Activate the Virtual Environment:**
   - **On Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

4. **Install the Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Populate the Database (Optional):**
   ```bash
   python manage.py populate_db
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

## Usage
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to access the application.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

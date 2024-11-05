from django.core.management.base import BaseCommand
from resume.models import User, SocialMedia, Experience, Skill, Language, Education


class Command(BaseCommand):
    help = "Populates the database with sample data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        SocialMedia.objects.all().delete()
        Experience.objects.all().delete()
        Skill.objects.all().delete()
        Language.objects.all().delete()
        Education.objects.all().delete()

        # Create a sample user
        user = User.objects.create_user(
            username="sahar",
            first_name="Sahar",
            last_name="Farahzad",
            email="s.farahzad91@gmail.com",
            phone_number="+989126475339",
            job_title="Backend Developer (Python / Django)",
            about="Backend developer with 4+ years of experience in developing and designing websites and applications. Experienced with all stages of development. Delivered overall 95% bug-free websites. Fast learner and committed to clean code and high-quality API. Passionate about learning new skills and modern technologies.",
            password="1234.qaz",  # Consider using an environment variable for the password
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )

        # Add sample social media links
        social_media_data = [
            {
                "platform": "LinkedIn",
                "url": "https://www.linkedin.com/in/sahar-farahzad-7b7559ba",
                "icon": "resume/icons/linkedin.png",
            },
            {
                "platform": "GitHub",
                "url": "https://github.com/TheSaharFarahzad",
                "icon": "resume/icons/github.png",
            },
            {
                "platform": "Twitter",
                "url": "",
                "icon": "resume/icons/twitter.png",
            },
            {
                "platform": "Address",
                "url": "https://www.google.com/maps/search/?api=1&query=Germany",
                "icon": "resume/icons/globe.png",
            },
            {
                "platform": "Medium",
                "url": "https://medium.com/@SSurvivor",
                "icon": "resume/icons/medium.png",
            },
            {
                "platform": "Stack Overflow",
                "url": "https://stackoverflow.com/users/11438105/codequest",
                "icon": "resume/icons/stackoverflow.png",
            },
        ]

        for data in social_media_data:
            SocialMedia.objects.create(user=user, **data)

        # Add sample experience
        experience_data = [
            {
                "company": "Fleetspark Co",
                "company_address": "Berlin, Germany",
                "start_date": "2020-09-01",
                "end_date": "2023-09-01",
                "still_working": False,
                "role": "Backend Developer",
                "task_description": (
                    "Contributing as a backend developer in AI-based driver coaching technology for truck operators using Django Rest Framework, Django, Python\n"
                    "Contributing as a backend developer in Driverless car rental using Django Rest Framework, Django, Python\n"
                    "Designing and developing new features, endpoints, and commands using TDD\n"
                    "Testing, debugging, and problem-solving using Python unit test, Pytest, Python shell, VScode debugger, and advanced packages like mock and patch\n"
                    "Optimizing database queries, loading speed, and more using django-debug-toolbar\n"
                    "Deploying the project into Jenkins using the Git version control system\n"
                    "Cooperating with other teams"
                ),
                "skills_used": [
                    "Django",
                    "Django Rest Framework",
                    "Python",
                    "Jenkins",
                    "Git",
                ],
            },
            {
                "company": "Sepehr Processing Company",
                "company_address": "Tehran, Iran",
                "start_date": "2020-01-01",
                "end_date": "2020-09-01",
                "still_working": False,
                "role": "Software Engineer",
                "task_description": (
                    "Debugging software using Python\n"
                    "Automating tasks with Python\n"
                    "Design and development of web-based systems using React.js, HTML, and CSS"
                ),
                "skills_used": ["Python", "React.js", "HTML", "CSS"],
            },
            {
                "company": "Iran Telecommunication Research Center (ITRC)",
                "company_address": "Tehran, Iran",
                "start_date": "2018-06-01",
                "end_date": "2019-12-31",
                "still_working": False,
                "role": "Software Engineer",
                "task_description": (
                    "Contributing as a backend developer in National Information Sharing and Analysis Center (ISAC) using Django Rest Framework (DRF)\n"
                    "Writing tests using Python unit test and Pytest\n"
                    "Designing ER Diagrams using GUI Design\n"
                    "Designing charts and tables using Material-UI, Highcharts, and DataTables libraries with React.js"
                ),
                "skills_used": [
                    "Django Rest Framework",
                    "Python",
                    "Material-UI",
                    "Highcharts",
                    "DataTables",
                    "React.js",
                ],
            },
            {
                "company": "Iran Telecommunication Research Center",
                "company_address": "Tehran, Iran",
                "start_date": "2017-08-01",
                "end_date": "2018-06-01",
                "still_working": False,
                "role": "Researcher",
                "task_description": (
                    "Contributing to the establishment of an industrial control systems testing laboratory by installation and investigation of Cyber Security Evaluation Tool (CSET)"
                ),
                "skills_used": ["Cyber Security Evaluation Tool (CSET)"],
            },
            {
                "company": "Freelancer",
                "company_address": "Tehran, Iran",
                "start_date": "2013-04-01",
                "end_date": "2014-07-01",
                "still_working": False,
                "role": "Freelancer",
                "task_description": (
                    "Web designing with HTML and CSS\n"
                    "Developed a warehouse handling application for Mehregan Metal Industries using Visual Basic"
                ),
                "skills_used": ["HTML", "CSS", "Visual Basic"],
            },
        ]

        for exp in experience_data:
            Experience.objects.create(user=user, **exp)

        # Add sample skills
        skills_data = [
            {"skill_name": "Python", "years_of_experience": 7},
            {"skill_name": "Django", "years_of_experience": 7},
            {"skill_name": "Django Rest Framework", "years_of_experience": 7},
            {"skill_name": "Linux ", "years_of_experience": 7},
            {"skill_name": "Git ", "years_of_experience": 7},
            {"skill_name": "APIs", "years_of_experience": 4},
            {"skill_name": "Postman", "years_of_experience": 4},
            {"skill_name": "PostgreSQL ", "years_of_experience": 4},
            {"skill_name": "MySQL ", "years_of_experience": 2},
            {"skill_name": "TDD ", "years_of_experience": 4},
            {"skill_name": "Docker", "years_of_experience": 4},
            {"skill_name": "Performance Optimization ", "years_of_experience": 2},
            {"skill_name": "Celery", "years_of_experience": 2},
            {"skill_name": "GraphQL", "years_of_experience": 2},
            {"skill_name": "Data Security & Privacy", "years_of_experience": 2},
            {"skill_name": "Django Channels", "years_of_experience": 0},
            {"skill_name": "NoSQL Databases(MongoDB|Redis)", "years_of_experience": 0},
            {"skill_name": "Kubernetes", "years_of_experience": 0},
            {"skill_name": "NumPy", "years_of_experience": 0},
            {"skill_name": "Pandas", "years_of_experience": 0},
            {"skill_name": "HTML, CSS", "years_of_experience": 1},
            {"skill_name": "Javascript", "years_of_experience": 1},
            {"skill_name": "Reactjs", "years_of_experience": 1},
        ]

        for skill in skills_data:
            Skill.objects.create(user=user, **skill)

        # Add sample languages
        languages_data = [
            {"language_name": "Persian", "proficiency_level": "native"},
            {"language_name": "English", "proficiency_level": "fluent"},
            {"language_name": "German", "proficiency_level": "intermediate"},
            {"language_name": "Turkish", "proficiency_level": "basic"},
            {"language_name": "Arabic", "proficiency_level": "basic"},
        ]

        for lang in languages_data:
            Language.objects.create(user=user, **lang)

        # Add sample education
        education_data = [
            {
                "university_name": "Payame Noor University",
                "university_address": "Tehran, Iran",
                "field_of_study": "Applied Mathematics",
                "degree": "bachelor",
                "start_date": "2014-09-01",
                "end_date": "2018-06-30",
                "still_studying": False,
            },
        ]

        for edu in education_data:
            Education.objects.create(user=user, **edu)

        self.stdout.write(self.style.SUCCESS("Database populated with sample data."))

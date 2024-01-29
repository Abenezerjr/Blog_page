# Blog_page

![Web capture_26-12-2023_174056_127 0 0 1](https://github.com/Abenezerjr/Blog_page/assets/106702572/4dbd41d4-7984-447d-9b9a-015a95491beb)

# Django Blog with All Oprations
This is a fully functional blog developed using Django and Bootstrap, featuring posts and a Django Blog with All CRDE Operation Include Authentication and add comment section store post read later session user registration And more.

## Features

- **Posts:** Create, edit, and delete blog posts.
- **Comments:** Users can leave comments on posts.
- **Replying to Comments:** Capability to reply to individual comments.
- **Bootstrap Styling:** Stylishly designed frontend using Bootstrap.
-**Authentication:** user register and login
-**Session:** user add read later  store
 -**Animation** some Animation for ux 
-**And MORE...** 
## Installation

1. Clone the repository:

    ```bash
    git clone [https://github.com/Abenezerjr/Blog_page.git]
    cd Blog_page/
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate  # Activate the virtual environment
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your browser at `http://localhost:8000`.

## Usage

1. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

2. Visit `http://localhost:8000/admin` and log in using the credentials created in the previous step.
   
3. Start managing posts and comments through the admin interface.

## Contributions

Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](Abenezerjb).

## Acknowledgements

Special thanks to [Django](https://www.djangoproject.com/) and [Bootstrap](https://getbootstrap.com/) for their fantastic frameworks.

---

Feel free to modify and expand upon this README to better reflect the features, setup instructions, and any other details specific to your Django blog project.


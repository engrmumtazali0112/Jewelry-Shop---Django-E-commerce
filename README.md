# Jewelry Shop - Django E-commerce Website 🛍️

A comprehensive web-based application designed to manage and streamline the operations of a jewelry shop. The system includes features for inventory management, order processing, customer management, and sales tracking. Developed using Django, the project provides an intuitive interface for both customers and shop staff, enabling efficient management of the shop's daily operations.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Django](https://img.shields.io/badge/django-5.0-green.svg)
## Live Demo

Check out the live demo of the Jewelry Shop platform:

![Live Demo](https://github.com/engrmumtazali0112/Jewelry-Shop---Django-E-commerce/blob/main/IMG_9022-ezgif.com-video-to-gif-converter.gif)

## ✨ Features

- 🔐 User Authentication System
  - Registration, Login, Logout
  - Password Reset
  - Profile Management
  - Address Management

- 🛍️ Shopping Features
  - Product Categories
  - Product Details
  - Shopping Cart
  - Order Management
  - Checkout Process

- 📝 Content Management
  - Blog System
  - Contact Form
  - About Page
  - Dynamic Category Navigation

- 💼 Admin Features
  - Product Management
  - Order Tracking
  - User Management
  - Content Management

## 📸 Screenshots

<details>
<summary>Click to view screenshots</summary>

### Main Page
[![Main Page](https://github.com/user-attachments/assets/451707d5-cad9-4db9-b8ed-7982b282f044)](https://github.com/user-attachments/assets/451707d5-cad9-4db9-b8ed-7982b282f044)

### Footer 
[![User Registration](https://github.com/user-attachments/assets/bd8441f4-598f-4af2-9435-96cb8741121b)](https://github.com/user-attachments/assets/bd8441f4-598f-4af2-9435-96cb8741121b)

### Product
[![User Login](https://github.com/user-attachments/assets/22c32f75-ae0e-4b2a-b4df-2dc73178ff6f)](https://github.com/user-attachments/assets/22c32f75-ae0e-4b2a-b4df-2dc73178ff6f)

### Catagories
[![Password Reset](https://github.com/user-attachments/assets/b78b9e44-26c6-44ce-80a1-04e67dc36e49)](https://github.com/user-attachments/assets/b78b9e44-26c6-44ce-80a1-04e67dc36e49)

### Cart
[![Admin Dashboard](https://github.com/user-attachments/assets/32237254-f341-4a34-a3b2-3b6a1f49a96f)](https://github.com/user-attachments/assets/32237254-f341-4a34-a3b2-3b6a1f49a96f)

### User Cart
[![Product Management](https://github.com/user-attachments/assets/fca0ea73-736f-407e-ba72-e676b962deca)](https://github.com/user-attachments/assets/fca0ea73-736f-407e-ba72-e676b962deca)

### Shopping Cart
[![Shopping Cart](https://github.com/user-attachments/assets/ce02f129-388b-467f-bf7f-4aab8e16b19f)](https://github.com/user-attachments/assets/ce02f129-388b-467f-bf7f-4aab8e16b19f)

### Checkout Page
[![Checkout Page](https://github.com/user-attachments/assets/ae6b5272-cc4d-4086-98c7-fbbb96d87c09)](https://github.com/user-attachments/assets/ae6b5272-cc4d-4086-98c7-fbbb96d87c09)

### Order Confirmation
[![Order Confirmation](https://github.com/user-attachments/assets/c7433100-ecac-4b4d-895d-e9dfb9a358ba)](https://github.com/user-attachments/assets/c7433100-ecac-4b4d-895d-e9dfb9a358ba)

### Payment Screen
[![Payment Screen](https://github.com/user-attachments/assets/d883eeeb-2365-437e-8b1d-19808e47d0b5)](https://github.com/user-attachments/assets/d883eeeb-2365-437e-8b1d-19808e47d0b5)

### Order History
[![Order History](https://github.com/user-attachments/assets/8aee81fa-fb7c-4c88-b0bd-e5c2c62cca63)](https://github.com/user-attachments/assets/8aee81fa-fb7c-4c88-b0bd-e5c2c62cca63)

### Admin Orders Management
[![Admin Orders Management](https://github.com/user-attachments/assets/5e061a35-c603-4067-8668-85c0d327db65)](https://github.com/user-attachments/assets/5e061a35-c603-4067-8668-85c0d327db65)

### Admin Product Management
[![Admin Product Management](https://github.com/user-attachments/assets/289ff619-5ea0-40cd-b115-39b1174e3100)](https://github.com/user-attachments/assets/289ff619-5ea0-40cd-b115-39b1174e3100)

</details>

### Prerequisites

- Python 3.x
- pip (Python package manager)
- virtualenv (recommended)

### Installation

1. Clone the repository
```bash
[git clone https://github.com/yourusername/Jewelry-Shop.git](https://github.com/engrmumtazali0112/Jewelry-Shop---Django-E-commerce.git)
cd Jewelry-Shop
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Copy example environment file
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Start development server
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/ in your browser

## 📁 Project Structure

```
jewelry_shop/
│
├── store/                      # Main app directory
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files
│   │   ├── css/
│   │   ├── js/
│   │   ├── img/
│   │   └── vendor/
│   ├── templates/             # HTML templates
│   │   ├── account/          # Account-related templates
│   │   └── store/            # Store-related templates
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── urls.py               # URL configurations
│   └── forms.py              # Form definitions
│
├── templates/                  # Base templates
├── media/                     # User-uploaded files
├── static/                    # Static files
└── manage.py                  # Django management script
```

## 🔧 Technology Stack

- **Backend**
  - Django 5.0
  - Python 3.x
  - SQLite (development)
  - PostgreSQL (production)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 4
  - Font Awesome

- **Payment Integration**
  - [Payment Gateway] (Coming Soon)

## 📝 Dependencies

```txt
Django>=5.0.0
Pillow>=10.0.0
django-crispy-forms>=2.1
django-environ>=0.11.2
django-widget-tweaks>=1.5.0
```

## 🛠️ Configuration

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```

## 👥 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

For support, email [your-email@example.com](mailto:your-email@example.com) or create an issue in the GitHub repository.

## 🙏 Acknowledgments

- Bootstrap Templates
- Django Documentation
- Font Awesome Icons
- All Contributors

## 📸 Screenshots

[Coming Soon]

## 🚀 Deployment

Detailed deployment instructions for various platforms:

### Heroku
```bash
# Install Heroku CLI
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

### DigitalOcean
[Deployment Guide Coming Soon]

## ⚙️ Development

To set up the development environment:

1. Ensure all dependencies are installed
```bash
pip install -r requirements-dev.txt
```

2. Run tests
```bash
python manage.py test
```

3. Check code style
```bash
flake8 .
```

## 📝 Todo

- [ ] Add payment gateway integration
- [ ] Implement wish list functionality
- [ ] Add product reviews and ratings
- [ ] Implement search functionality
- [ ] Add product recommendations

## 🔄 Version History

* 0.1
    * Initial Release
    * Basic e-commerce functionality

## 📊 Status

Project is: _in progress_

# 📌 Follow Us

📜 License
This repository is licensed under the MIT License.
<p align="center">
  <a href="mailto:engrmumtazali01@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/mumtaz-ali"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://www.instagram.com/its_maliyzi"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
  <a href="https://x.com/mumtazali1223/status/1846913595021328672?s=51"><img src="https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=x&logoColor=white"/></a>
  <a href="https://discord.gg/DZgwHzEb"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white"/></a>
  <a href="https://wa.me/923476338292" target="_blank"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a>
   <a href="https://www.hackerrank.com/profile/engrmumtazali01" target="_blank">
  <img src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white"/>
</a>
</p>

<p align="center">Made with ❤️ by Mumtaz Ali</p>

**Happy coding!** ✨

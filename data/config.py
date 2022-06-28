from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5531631190:AAHyWlBfiCP2OYB7r-ykZAJfm0HmMIg0cW0"  # Bot toekn
ADMINS = [5332814623]  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

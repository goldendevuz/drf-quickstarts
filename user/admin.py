from django.contrib.auth import get_user_model
import data_wizard

User = get_user_model()

data_wizard.register(User)
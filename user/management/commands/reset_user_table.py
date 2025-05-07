import os
from django.core.management.base import BaseCommand
from django.db import connection
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Deletes all records and resets auto-increment for the User table"

    def handle(self, *args, **kwargs):
        self.reset_table(User)

    def reset_table(self, model):
        table_name = model._meta.db_table

        # Delete all records
        model.objects.all().delete()
        self.stdout.write(f"🗑️ Deleted all records from {table_name}.")

        # Reset auto-increment
        with connection.cursor() as cursor:
            if connection.vendor == 'postgresql':
                sequence_name = f"{table_name}_id_seq"
                cursor.execute(f"ALTER SEQUENCE {sequence_name} RESTART WITH 1;")
                self.stdout.write(f"✅ PostgreSQL: Auto-increment reset for {table_name}.")
            elif connection.vendor == 'mysql':
                cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")
                self.stdout.write(f"✅ MySQL/MariaDB: Auto-increment reset for {table_name}.")
            elif connection.vendor == 'sqlite':
                cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}';")
                self.stdout.write(f"✅ SQLite: Auto-increment reset for {table_name}.")
            else:
                self.stdout.write("❌ Unsupported database type.")

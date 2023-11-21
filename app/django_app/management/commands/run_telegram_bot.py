from django.core.management.base import BaseCommand
import telebot
from django_app.models import Task


bot = telebot.TeleBot("6557769679:AAGKh8WTMP57DX6QyW2yaREb4pL1sz8Lv2s") # Вставьте сюда свой токен


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['tasks'])
def tasks(message):
    tasks = Task.objects.all()
    for task in tasks:
        bot.send_message(message.chat.id, task.title)

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = "Available commands:\n"
    help_text += "/start - Start the bot\n"
    help_text += "/tasks - List all tasks\n"
    help_text += "/help - Show this help message"
    help_text += "/add <task_title> <task_description> <task_status> - Add a new task"
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['add'])
def add_task(message):
    # Extract the task details from the command message
    command_parts = message.text.split(' ', 4)
    
    if len(command_parts) < 5:
        bot.send_message(message.chat.id, "Invalid command format. Use /add <task_title> <task_description> <task_status>")
        return

    task_title = command_parts[1]
    task_description = command_parts[2]
    task_status = command_parts[3]

    # Create a new task and save it to the database
    new_task = Task(title=task_title, description=task_description, status=task_status)
    new_task.save()

    bot.send_message(message.chat.id, f"Task '{task_title}' added successfully!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")



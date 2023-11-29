from django.test import TestCase
from .models import Task  # Replace 'yourapp' with the actual name of your Django app

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task description.',
            status='TODO'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task description.')
        self.assertEqual(self.task.status, 'TODO')

    def test_task_update_status(self):
        self.task.status = 'IN_PROGRESS'
        self.task.save()
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.status, 'IN_PROGRESS')

    def test_task_str_representation(self):
        expected_str = 'Test Task'
        self.assertEqual(str(self.task), expected_str)

from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskCreationTests(TestCase):
    def test_store_task_persists_posted_task(self):
        response = self.client.post(
            reverse('store_task'),
            {'title': 'Buy milk', 'description': 'Get milk from the store'},
        )

        self.assertRedirects(response, reverse('tasks_list'))
        task = Task.objects.get(title='Buy milk')
        self.assertEqual(task.description, 'Get milk from the store')
        self.assertFalse(task.is_completed)

    def test_checked_task_is_saved_as_completed(self):
        self.client.post(
            reverse('store_task'),
            {
                'title': 'Finished task',
                'description': 'Already done',
                'is_completed': 'on',
            },
        )

        self.assertTrue(Task.objects.get(title='Finished task').is_completed)

    def test_tasks_list_does_not_display_saved_tasks_yet(self):
        Task.objects.create(title='Saved task', description='Not shown yet')

        response = self.client.get(reverse('tasks_list'))

        self.assertNotContains(response, 'Saved task')
        self.assertNotContains(response, 'Not shown yet')

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

    def test_tasks_list_displays_edit_link_for_saved_tasks(self):
        task = Task.objects.create(title='Saved task', description='Saved description')

        response = self.client.get(reverse('tasks_list'))

        self.assertContains(response, 'Saved task')
        self.assertContains(response, reverse('edit_task', args=[task.id]))

    def test_edit_task_updates_saved_task(self):
        task = Task.objects.create(
            title='Old title',
            description='Old description',
            is_completed=False,
        )

        response = self.client.post(
            reverse('edit_task', args=[task.id]),
            {
                'title': 'Updated title',
                'description': 'Updated description',
                'is_completed': 'on',
            },
        )

        self.assertRedirects(response, reverse('tasks_list'))
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated title')
        self.assertEqual(task.description, 'Updated description')
        self.assertTrue(task.is_completed)

    def test_edit_task_get_displays_existing_values(self):
        task = Task.objects.create(
            title='Existing title',
            description='Existing description',
            is_completed=True,
        )

        response = self.client.get(reverse('edit_task', args=[task.id]))

        self.assertContains(response, 'value="Existing title"')
        self.assertContains(response, 'Existing description')
        self.assertContains(response, 'checked')

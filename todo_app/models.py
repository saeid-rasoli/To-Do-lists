from django.db import models
from django.utils import timezone
from django.urls import reverse

# due date from week
def once_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class TodoList(models.Model):
    title = models.CharField(max_length=250, unique=True)
    
    def get_absolute_url(self):
        return reverse("list", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return self.title
    
class TodoItem(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=once_week_hence)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ['due_date']
    
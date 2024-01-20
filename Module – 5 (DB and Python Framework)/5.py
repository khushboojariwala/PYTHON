"""
What is a QuerySet?Write program to create a new Post object in
database:

In Django, a QuerySet is a collection of database queries applied to a model. It allows you to interact with your database using a high-level abstraction, enabling you to retrieve, filter, and manipulate data from your database without writing raw SQL queries.

A QuerySet is created when you query the database for instances of a model. You can further refine the QuerySet by chaining methods like filter(), exclude(), and order_by() to narrow down the results. Finally, when you need to execute the query and retrieve the actual data, you can use methods like get(), all(), or iteration.

Here's an example program that demonstrates creating a new Post object and saving it to the database in Django:

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

Now, let's create a new Post object and save it to the database using Django's QuerySet:

# myapp/models.py
from blog.models import Post

# Create a new Post object
new_post = Post(
    title="Sample Post",
    content="This is the content of the sample post.",
)

new_post.save()

# Access the fields of the saved Post object
print("Post Title:", new_post.title)
print("Post Content:", new_post.content)
print("Publication Date:", new_post.pub_date)

"""
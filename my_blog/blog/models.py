from django.db import models

# Create your models here.
class Tag(models.Model):
    caption= models.CharField(max_length=20)

    def __str__(self):
        return f"{caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.CharField(max_length=30)

    def full_name(self):
        return f"{first_name} {last_name}    {email_address}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=20)
    excerpt = models.CharField(max_length=50)
    image_name = models.CharField(max_length=20)
    date = models.DateField()
    slug = models.SlugField(max_length=20)
    content = models.CharField(max_length=200)
    author=models.ForeignKey(Author, on_delete= models.PROTECT, null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return f"""
            Title: {title},
            Excerpt: {excerpt},
            Image name: {image_name},
            Date: {date}
            Slug: {slug}
            Content: {content}
        """
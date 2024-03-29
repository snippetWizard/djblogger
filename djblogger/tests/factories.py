import factory
from django.contrib.auth.models import User
from djblogger.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = "test"
    password = "test"
    is_superuser  = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "X"
    subtitle = "X"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "X"
    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return 
        if extracted:
            self.tags.add(extracted)
        else:
            self.tags.add(
                "Python",
                "Django",
                "Database",
                "Pytest",
                "JavaScript",
                "VSCode",
                "Deployment",
                "Full-Stack",
                "ORM",
                "Front-End",
                "Back-End",
            )
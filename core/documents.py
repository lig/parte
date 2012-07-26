from datetime import datetime

from django.db.models import permalink
from mongoengine import *
from mongoengine.django.auth import User


class Post(Document):

    user = ReferenceField(User, required=True)
    created = DateTimeField()
    updated = DateTimeField()
    text = StringField(required=True)

    meta = {
        'ordering': ['-created']
    }

    def save(self, *args, **kwargs):
        now = datetime.utcnow()

        if not self.pk:
            self.created = self.updated = now
        elif any(self._delta()):
            self.updated = now

        super(Post, self).save()

    @permalink
    def get_absolute_url(self):
        return ('posts-post', (self.pk,))

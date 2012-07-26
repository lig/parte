from datetime import datetime

from django.db.models import permalink
from mongoengine import *
from mongoengine.django.auth import User


class Comment(EmbeddedDocument):

    user = ReferenceField(User, required=True)
    created = DateTimeField()
    text = StringField(required=True)


class Post(Document):

    user = ReferenceField(User, required=True)
    created = DateTimeField()
    updated = DateTimeField()
    text = StringField(required=True)
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {
        'ordering': ['-created']
    }

    def save(self, *args, **kwargs):
        print self.comments, type(self.comments)
        now = datetime.utcnow()

        if not self.created:
            self.created = now

        if any(self._delta()):
            self.updated = now

        for i in range(len(self.comments)):

            if not self.comments[i].created:
                self.comments[i].created = now

        super(Post, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('posts-post', (self.pk,))

    def add_comment(self, comment):
        comment.created = datetime.utcnow()
        Post.objects(pk=self.pk).update_one(push__comments=comment)

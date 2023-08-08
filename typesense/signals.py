from django.db.models.signals import post_delete, post_save

from .models import Post
from .utils import client


@receiver(post_save, sender=Post)
def update_typesense_posts(sender, instance, created, **kwargs):
    if instance:
       try:  
          document = {
                  'id': str(instance.id),
                  'title': str(instance.title),
                  'subject': str(instance.description)
              }
          client.collections['posts'].documents.upsert(
                  document)
        
       except Exception as e:
          print(e)


@receiver(post_delete,sender=Post)
def delete_typesense_posts(sender,instance,*args,**kwargs):
    try:
        client.collections['posts'].documents[str(instance.id)].delete()
    except:
        pass
from django.core.management.base import BaseCommand, CommandParser

from .models import Post
from .utils import client  # connection object


class Command(BaseCommand):
    help = 'Custom console command django'

    def add_arguments(self, parser):
        parser.add_argument('command_name', type=str,
                            help='Run python .\manage.py typesensepro schema , python manage.py  typesensepro reindex python manage.py  typesensepro delete')
        
        def handle(self, *args, **kwargs):
            command_name = kwargs['command_name']

            if client.operations.is_healthy():
                if command_name == 'schema':
                    schema = {
                         'name': 'posts',
                    'fields': [
                        {
                            'name':  'title',
                            'type':  'string',
                        },
                        {
                            'name':  'description',
                            'type':  'string',
                        }
                    ],
                }
                    
                try:
                    res = client.collections.create(schema)
                    print(res)
                except Exception as e:
                    print(e)

            elif command_name == 'destroy':
                try:
                    res = client.collections['posts'].delete()
                    print(res)
                except Exception as e:
                    print(e)
            elif command_name == 'reindex':
                try:

                    posts = Post.objects.all()
                    
                    for post in posts:
 
                        document = {
                            'id': str(post.id),
                            'title': str(post.title),
                            'description': str(post.description)
                        }
                        res = client.collections['posts'].documents.upsert(
                            document)
                        print(post.id)
                        
                except Exception as e:
                    print(e)
            
            else:
                print("Typesense disconnected or error occoured")

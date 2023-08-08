from decouple import config

import typesense


client = typesense.Client({
    'api_key': config('TYPESENSE_KEY'),
            'nodes': [{
                'host': config('TYPESENSE_IP'),
                'port': config('TYPESENSE_PORT'),
                'protocol': 'http'
            }],
            'connection_timeout_seconds': 2
})
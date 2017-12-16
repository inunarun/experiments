import json
overrides = dict()

overrides.update(**{
    'david': {
        'neo4j_url': 'bolt://796bafef-staging.databases.neo4j.io',
        'neo4j_user': 'readonly',
        'neo4j_password': '0s3DGA6Zq'
    },
    'floydhub': { # Todo: implement me?

    },
    'local': { # Just uses defaults

    }
})

with open('./config/local_overrides.json') as f:
    overrides.update(json.load(f))
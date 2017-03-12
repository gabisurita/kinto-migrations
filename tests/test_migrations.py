import unittest

from kinto_http import Client

from kinto_migrations import migrate_model


class BasicMigrationsTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(server_url='http://localhost:8888/v1/',
                             auth=('test', 'case'))

    def test_create_bucket(self):
        model = {
            '$buckets': {
                'stuff': {}
            }
        }

        migrate_model(self.client, model)
        self.client.get_bucket('stuff')

    def test_create_collection(self):
        model = {
            '$buckets': {
                'stuff': {
                    '$collections': {
                        'good_stuff': {}
                    }
                }
            }
        }

        migrate_model(self.client, model)
        self.client.get_collection('good_stuff', bucket='stuff')

    def test_create_record(self):
        model = {
            '$buckets': {
                'stuff': {
                    '$collections': {
                        'good_stuff': {
                            '$records': {
                                'bitcoin': {}
                            }
                        }
                    }
                }
            }
        }

        migrate_model(self.client, model)
        self.client.get_record('bitcoin',
                               bucket='stuff',
                               collection='good_stuff')

    def test_support_metadata(self):
        model = {
            '$buckets': {
                'stuff': {
                    'foo': 'bar'
                }
            }
        }
        migrate_model(self.client, model)
        data = self.client.get_bucket('stuff')['data']
        assert data['foo'] == 'bar'

    def test_support_permissions(self):
        model = {
            '$buckets': {
                'stuff': {
                    '$permissions': {
                        'read': ['bar']
                    }
                }
            }
        }
        migrate_model(self.client, model)
        perms = self.client.get_bucket('stuff')['permissions']
        assert 'bar' in perms['read']

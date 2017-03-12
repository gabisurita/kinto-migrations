def migrate_model(client, model):
    """Create or update Kinto resources specified on a model object.

    :param client: Kinto http client.
    :param model: Mapping representing a kinto model.
    """

    buckets = model.get('$buckets', {})

    with client.batch() as batch:
        for bucket_id, bucket in buckets.items():

            groups = bucket.pop('$groups', {})
            collections = bucket.pop('$collections', {})
            permissions = bucket.pop('$permissions', {})

            batch.update_bucket(bucket_id,
                                data=bucket,
                                permissions=permissions)

            for group_id, group in groups.items():

                permissions = group.pop('$permissions', {})
                group.setdefault('members', [])

                batch.update_group(group_id,
                                   bucket=bucket_id,
                                   data=group,
                                   permissions=permissions)

            for collection_id, collection in collections.items():

                records = collection.pop('$records', {})
                permissions = collection.pop('$permissions', {})

                batch.update_collection(collection=collection_id,
                                        bucket=bucket_id,
                                        data=collection,
                                        permissions=permissions)

                for record_id, record in records.items():

                    permissions = record.pop('$permissions', {})

                    batch.update_record(id=record_id,
                                        bucket=bucket_id,
                                        collection=collection_id,
                                        data=record,
                                        permissions=permissions)

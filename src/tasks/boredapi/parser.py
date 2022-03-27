from src.database.models.activity import Activity


def parse_boredapi(ti):
    raw_data = ti.xcom_pull(key='extracted_data', task_ids='extract')

    activities = []

    unique_activities = [i for n, i in enumerate(raw_data) if i not in raw_data[n + 1:]]

    for a in unique_activities:
        name = a['activity'].replace("'", "") or ''
        kind = a['type'] or ''
        participants = a['participants']
        price = round(a['price'], 2)

        activity = Activity(name=name, kind=kind, participants=participants,
                            price=price)

        activities.append(activity)

    ti.xcom_push(key='parsed_data', value=activities)

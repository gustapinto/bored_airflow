from concurrent.futures import as_completed

from requests_futures.sessions import FuturesSession


def extract_boredapi(ti):
    ENDPOINT = 'https://www.boredapi.com/api/activity'
    TOTAL = 1000

    data = []
    futures = []

    session = FuturesSession()

    for i in range(0, TOTAL):
        future = session.get(ENDPOINT)
        future.i = i

        futures.append(future)

    for future in as_completed(futures):
        response = future.result()

        data.append(response.json())

    ti.xcom_push(key='extracted_data', value=data)

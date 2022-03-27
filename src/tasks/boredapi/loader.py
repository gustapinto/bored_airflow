from sqlalchemy.orm import Session

from src.database.database import engine


def load_boredapi(ti):
    activities = ti.xcom_pull(key='parsed_data', task_ids='parse')

    with Session(engine) as session, session.begin():
        session.add_all(activities)
        session.commit()

import os

from sqlalchemy import create_engine,text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
 connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    result_all = result.fetchall()
    jobs = [dict(zip(result.keys(), row)) for row in result_all]
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from jobs WHERE id ={id}"))
    rows = result.fetchall()

    if len(rows) == 0:
      return None
    else :
      return rows[0]._asdict()

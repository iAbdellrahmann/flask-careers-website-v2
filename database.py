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
    

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications(job_id, name, email, linkedin, education, workexp, resume) VALUES (:job_id, :name, :email, :linkedin, :education, :workexp, :resume)")
        params = {'job_id': job_id, 'name': data['name'], 'email': data['email'], 'linkedin': data['linkedin'], 'education': data['education'], 'workexp': data['workexp'], 'resume': data['resume']}
        conn.execute(query, params)
     

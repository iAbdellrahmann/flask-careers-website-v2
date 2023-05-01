from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://j26ijm4wpt2wzm03xp73:pscale_pw_gvvsKwbOvvzuIeWKEMfksU24pY7rNxAiu3JOsfZbnUl@aws.connect.psdb.cloud/jobs?charset=utf8mb4",
 connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())
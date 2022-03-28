import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler  # other schedulers are available
from fastapi import FastAPI
from fastapi_sqlalchemy import db

from app.models import User, UserCount

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="sqlite://")


@app.on_event('startup')
async def startup_event():
    scheduler = AsyncIOScheduler(timezone=pytz.utc)
    scheduler.start()
    scheduler.add_job(count_users_task, "cron", hour=0)  # runs every night at midnight


def count_users_task():
    """Count the number of users in the database and save it into the user_counts table."""

    # we are outside of a request context, therefore we cannot rely on ``DBSessionMiddleware``
    # to create a database session for us. Instead, we can use the same ``db`` object and
    # use it as a context manager, like so:

    with db():
        user_count = db.session.query(User).count()

        db.session.add(UserCount(user_count))
        db.session.commit()

    # no longer able to access a database session once the db() context manager has ended

    return users
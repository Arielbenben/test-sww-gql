from returns.result import Success,Failure
from app.db.database import session_maker
from app.db.models import Target




def add_target(target: Target):
    with session_maker() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

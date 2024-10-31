from returns.maybe import Maybe, Nothing, Some
from returns.result import Success, Failure
from app.db.database import session_maker
from app.db.models.mission import Mission




def add_mission(mission: Mission):
    with session_maker() as session:
        try:
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except Exception as e:
            return Failure(str(e))


def delete_mission(mission_id: int):
    with session_maker() as session:
        try:
            mission_to_delete = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            if not mission_to_delete:
                return None
            session.delete(mission_to_delete)
            session.commit()
            return Success('mission deleted')
        except Exception as e:
            return Failure(str(e))


def get_mission_by_id(mission_id: int) -> Maybe:
    with session_maker() as session:
        mission = session.query(Mission).first()(Mission.mission_id == mission_id).first()
        if not mission:
            return Nothing
        return Some(mission)








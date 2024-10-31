from graphql import GraphQLError
from returns.maybe import Maybe, Nothing, Some
from returns.result import Success, Failure
from sqlalchemy import func
from app.db.database import session_maker
from app.db.models import Mission, Target, TargetType,City,Country


def add_mission(mission: Mission):
    with session_maker() as session:
        try:
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except Exception as e:
            session.rollback()
            return Failure(str(e))


def delete_mission(mission_id: int):
    with session_maker() as session:
        try:
            mission_to_delete = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            if not mission_to_delete:
                raise GraphQLError(f'mission by the id: {mission_id} not found')
            session.delete(mission_to_delete)
            session.commit()
            return Success('mission deleted')
        except Exception as e:
            return Failure(str(e))


def get_mission_by_id(mission_id: int) -> Maybe:
    with session_maker() as session:
        mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
        if not mission:
            return Nothing
        return Some(mission)


def get_missions_between_dates(start_date, end_date):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date > start_date, Mission.mission_date < end_date).all()


def get_mission_by_target_industry(target_industry: str):
    with session_maker() as session:
        return session.query(Mission).join(Mission.target).filter(Target.target_industry == target_industry).all()


def get_mission_by_country_attack(mission_country: str):
    with session_maker() as session:
        return session.query(Mission
                             ).join(Mission.target).join(Target.city).join(City.country).filter(Country.country_name == mission_country).all()


def get_mission_results_by_target_type(target_type: str):
    with (session_maker() as session):
        return session.query(Mission
                             ).join(Mission.target).join(Target.target_type).filter(TargetType.target_type_name == target_type).all()


def update_mission_results(mission_id: int, aircraft_returned: float, aircraft_failed: float,
                           aircraft_damaged: float, aircraft_lost: float):
    with session_maker() as session:
        try:
            mission_to_update = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            if not mission_to_update:
                raise GraphQLError(f'mission by the id: {mission_id} not found')
            mission_to_update.aircraft_returned = aircraft_returned
            mission_to_update.aircraft_failed = aircraft_failed
            mission_to_update.aircraft_damaged = aircraft_damaged
            mission_to_update.aircraft_lost = aircraft_lost
            session.commit()
            session.refresh(mission_to_update)
            return Success(mission_to_update)
        except Exception as e:
            return Failure(str(e))


def get_statistics_on_missions_by_city(city_name: str):
    with (session_maker() as session):
        number_missions = len(session.query(Mission).join(Mission.target)
                                         .join(Target.city).filter(City.city_name == city_name).all())
        average_priority = session.query(func.avg(Target.target_priority)).join(Target.city).filter(
            (City.city_name == city_name) & (Target.target_priority != None)
        ).scalar()
        return [number_missions, average_priority]





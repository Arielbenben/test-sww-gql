from graphene import ObjectType, Field,Int

from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import get_mission_by_id


class Query(ObjectType):
    get_all_students = List(StudentType)
    get_mission_by_id = Field(MissionType, mission_id=Int(required=True))




    @staticmethod
    def resolve_get_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id).unwrap()


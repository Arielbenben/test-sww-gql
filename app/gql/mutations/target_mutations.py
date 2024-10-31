from graphene import Mutation, Int, String, Field, Boolean,Date,Float
from app.db.models.mission import Mission
from app.db.models.target import Target
from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import add_mission, delete_mission


class AddTarget(Mutation):
    class Arguments:
        mission_id = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        target_to_insert = Target(mission_id=mission_id)
        add_mission(target_to_insert)
        return AddTarget(mission=target_to_insert)
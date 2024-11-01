from graphene import Mutation,Int, String, Field
from app.db.models import Target
from app.gql.types.target_type import TargetType
from app.repository.target_repository import add_target



class AddTarget(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        target_industry = String(required=True)
        city_id = Int(required=True)
        target_type_id = Int(required=True)
        target_priority = Int(required=True)

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, mission_id, target_industry, city_id, target_type_id, target_priority):
        target_to_insert = Target(mission_id=mission_id, target_industry=target_industry, city_id=city_id,
                                  target_type_id=target_type_id, target_priority=target_priority)
        add_target(target_to_insert)
        return AddTarget(target=target_to_insert)


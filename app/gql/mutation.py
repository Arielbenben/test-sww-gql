from graphene import ObjectType
from app.gql.mutations.mission_mutations import AddMission, DeleteMission, UpdateMission
from app.gql.mutations.target_mutations import AddTarget




class Mutation(ObjectType):
    add_mission = AddMission.Field()
    delete_mission = DeleteMission.Field()
    add_target = AddTarget.Field()
    update_mission_results = UpdateMission.Field()

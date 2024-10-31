from graphene import Mutation, Int, Field, Boolean,Date,Float
from app.db.models import Mission
from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import add_mission, delete_mission, update_mission_results


class AddMission(Mutation):
    class Arguments:
        mission_date = Date(required=True)
        airborne_aircraft = Float(required=True)
        attacking_aircraft = Float(required=True)
        bombing_aircraft = Float(required=True)

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_date, airborne_aircraft, attacking_aircraft, bombing_aircraft):
        mission_to_insert = Mission(mission_date=mission_date, airborne_aircraft=airborne_aircraft, attacking_aircraft=attacking_aircraft,
                          bombing_aircraft=bombing_aircraft)
        add_mission(mission_to_insert)
        return AddMission(mission=mission_to_insert)


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    success = Field(Boolean)

    @staticmethod
    def mutate(root, info, mission_id):
        delete_mission(mission_id)
        return DeleteMission(success=True)


class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost):
        mission_updated = (update_mission_results(mission_id, aircraft_returned, aircraft_failed, aircraft_damaged, aircraft_lost)
                           .unwrap())
        return UpdateMission(mission=mission_updated)



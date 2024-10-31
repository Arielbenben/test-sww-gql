from graphene import ObjectType,Int,Date,Float




class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date(required=True)
    airborne_aircraft = Float(required=True)
    attacking_aircraft = Float(required=True)
    bombing_aircraft = Float(required=True)
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()

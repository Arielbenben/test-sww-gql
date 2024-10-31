from graphene import ObjectType,Int,String,Date,Float




class MissionType(ObjectType):
    id = Int()
    region = String()
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()
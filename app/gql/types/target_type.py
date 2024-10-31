from graphene import ObjectType,Int,String


class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int(required=True)
    target_industry = String(required=True)
    city_id = Int(required=True)
    target_type_id = Int(required=True)
    target_priority = String(required=True)


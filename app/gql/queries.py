from graphene import ObjectType, Field, Int, List, Date, String, Float
from app.gql.types.mission_type import MissionType
from app.repository.mission_repository import get_mission_by_id, get_missions_between_dates, \
    get_mission_by_country_attack, get_mission_by_target_industry, get_mission_results_by_target_type, \
    get_statistics_on_missions_by_city


class Query(ObjectType):
    get_mission_by_id = Field(MissionType, mission_id=Int(required=True))
    get_missions_between_dates = List(MissionType, start_date=Date(required=True), end_date=Date(required=True))
    get_missions_by_country_attack = List(MissionType, m_country_attack=String(required=True))
    get_missions_by_target_industry = List(MissionType, target_industry=String(required=True))
    get_missions_results_by_target_type = List(MissionType, target_type=String(required=True))
    get_statistic_on_missions_by_name = Float(city_name=String(required=True)), Float()


    @staticmethod
    def resolve_get_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id).unwrap()

    @staticmethod
    def resolve_get_missions_between_dates(root, info, start_date, end_date):
        return get_missions_between_dates(start_date, end_date)

    @staticmethod
    def resolve_get_missions_by_country_attack(root, info, m_country_attack):
        return get_mission_by_country_attack(m_country_attack)

    @staticmethod
    def resolve_get_missions_by_target_industry(root, info, target_industry):
        return get_mission_by_target_industry(target_industry)

    @staticmethod
    def resolve_get_missions_results_by_target_type(root, info, target_type):
        return get_mission_results_by_target_type(target_type)

    @staticmethod
    def resolve_get_statistic_on_missions_by_name(root, info, city_name):
        return get_statistics_on_missions_by_city(city_name)




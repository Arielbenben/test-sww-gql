



class Query(ObjectType):
    get_all_students = List(StudentType)
    get_student_by_id = Field(StudentType, id=Int(required=True))
    get_all_countries = List(CountryType)
    get_country_by_id = Field(CountryType, id=Int(required=True))
    get_all_vacations = List(StudentVacationType)
    get_vacation_by_id = Field(StudentVacationType, id=Int(required=True))



    @staticmethod
    def resolve_get_all_students(root, info):
        return get_all_students()
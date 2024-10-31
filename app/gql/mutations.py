



class Mutation(ObjectType):
    add_student = AddStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()
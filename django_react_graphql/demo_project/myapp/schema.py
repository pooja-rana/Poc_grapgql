import graphene
from graphene_django import DjangoObjectType

from .models import UserModel


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return UserModel.objects.all()


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    middal_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()

    class Arguments:
        first_name = graphene.String()
        middal_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    def mutate(self, info, first_name, middal_name, last_name, email):
        user = UserModel(first_name=first_name, middal_name=middal_name, last_name=last_name, email=email)
        user.save()

        return CreateUser(
            id=user.id,
            first_name=user.first_name,
            middal_name=user.middal_name,
            last_name=user.last_name,
            email=user.email
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


def get_followers(user):
    # devuelve una lista con los PK de los usuarios de las relaciones en las que el usuario <user> es relationship_target
    # followers_pks = user.relationship_target.all().values_list('origin', flat=True)
    # return list(User.objects.filter(pk__in=followers_pks))
    relationships = user.relationship_target.select_related('origin')
    followers = list()
    for relationship in relationships:
        followers.append(relationship.origin)
    return followers


def get_following(user):
    relationships = user.relationship_origin.select_related('target')
    following = list()
    for relationship in relationships:
        following.append(relationship.target)
    return following
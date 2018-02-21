from order_system_app.models import Customer

def create_user_by_type(backend, user, response, *args, **kwargs):
    request = backend.strategy.request_data()
    if backend.name == 'facebook':
        avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']

    if request['user_type'] == "customer" and not Customer.objects.filter(user_id=user.id):
        Customer.objects.create(user_id=user.id,avatar=avatar)


##pipeline is to create customer and other type of users

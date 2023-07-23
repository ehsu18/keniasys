from . import products, configurations, providers, clients, users, ventas


class ProductsDB(products.Database):
    pass


class ConfigurationsDB(configurations.Database):
    pass


class ProvidersDB(providers.Database):
    pass


class ClientsDB(clients.Database):
    pass

class UsersDB(users.Database):
    pass

class VentasDB(ventas.Database):
    pass

# TODO make a class for bills and the back of them
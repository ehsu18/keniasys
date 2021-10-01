from . import products, configurations, providers, clients


class ProductsDB(products.Database):
    pass


class ConfigurationsDB(configurations.Database):
    pass


class ProvidersDB(providers.Database):
    pass


class ClientsDB(clients.Database):
    pass

# TODO make a class for bills and the back of them
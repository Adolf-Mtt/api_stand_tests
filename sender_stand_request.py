import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
#    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_create_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, headers=data.headers)

def post_kit_products(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.KIT_PRODUCTS_PATH,
                         json=products_ids, headers=data.headers)
# post_products_kits(data.product_ids)


















# response_docs = get_docs()
# response_logs = get_logs()
# response_table = get_tabel()

# print('1T°', response_table.text)
# print()
# print('2U°', response_table.status_code)

# print('1°', response.headers)
# print()
# print('2°', response.status_code)
#
# print()
# print()
# print('one°', rspns.headers)
# print()
# print('two°', rspns.status_code)
# print()
# print('tree°', rspns.text)



#! /usr/bin/env python3
"""
    database_manager_test.py - Database Manager Test
    Author:
        - Hoanh An (hoanhan@bennington.edu)
    Date: 12/2/2017
"""

from database_manager import DatabaseManager
from pprint import pprint

if __name__ == '__main__':
    db_manager = DatabaseManager()

    # db_manager.operate_on_link_relation('INSERT', url='stuff1.com', chunk_id=1)
    # db_manager.operate_on_link_relation('INSERT', url='stuff2.com', chunk_id=1)
    # db_manager.operate_on_link_relation('INSERT', url='stuff3.com', chunk_id=1)
    # db_manager.operate_on_link_relation('UPDATE_STATE', url='stuff2.com', state='OK')
    # db_manager.operate_on_link_relation('DELETE', url='stuff3.com')


    # db_manager.operate_on_chunk_relation('INSERT', chunk_id=7)
    # db_manager.operate_on_chunk_relation('UPDATE_STATE', chunk_id=7, state='OK')
    # db_manager.operate_on_chunk_relation('DELETE', chunk_id=7)


    # db_manager.operate_on_host_relation('INSERT', host='10.10.127.112:5000', type='Crawler')
    # db_manager.operate_on_host_relation('UPDATE_STATE', host='10.10.127.111:5000', state='online')
    # db_manager.operate_on_host_relation('UPDATE_HEALTH', host='10.10.127.112:5000', health='healthy')
    # db_manager.operate_on_host_relation('UPDATE_STATE', host='10.10.127.112:5000', state='online')
    # db_manager.operate_on_host_relation('DELETE', host='10.10.127.111:5000')


    # db_manager.operate_on_crawler_relation('INSERT', chunk_id=1, host='10.10.127.100:5000')
    # db_manager.operate_on_crawler_relation('INSERT', chunk_id=1, host='10.10.127.100:5000')
    # db_manager.operate_on_crawler_relation('UPDATE_TASK', chunk_id=1, task='crawled')
    # db_manager.operate_on_crawler_relation('DELETE', chunk_id=1)


    # db_manager.operate_on_index_builder_relation('INSERT', chunk_id=10, host='10.10.127.102:5000')
    # db_manager.operate_on_index_builder_relation('UPDATE_TASK', chunk_id=1, task='built')
    # db_manager.operate_on_index_builder_relation('DELETE', chunk_id=1)


    # db_manager.operate_on_index_server_relation('INSERT', row=2, chunk_id=2, host='10.10.127.103:5000')
    # db_manager.operate_on_index_server_relation('UPDATE_ROW', row=3, chunk_id=3, host='10.10.127.104:5000')
    # db_manager.operate_on_index_server_relation('UPDATE_CHUNK_ID', chunk_id=6, row=3,  host='10.10.127.104:5000')
    # db_manager.operate_on_index_server_relation('UPDATE_HOST', host='10.10.127.101:5000', row=4, chunk_id=2)
    # db_manager.operate_on_index_server_relation('DELETE', chunk_id=6)


    # db_manager.__delete_relation__('link')


    # pprint(db_manager.get_relation('link'))
    # pprint(db_manager.get_relation('chunk'))
    # pprint(db_manager.get_relation('host'))
    # pprint(db_manager.get_relation('crawler'))
    # pprint(db_manager.get_relation('index_builder'))
    # pprint(db_manager.get_relation('index_server'))


    pprint(db_manager.get_all_relations_for_all_chunks())
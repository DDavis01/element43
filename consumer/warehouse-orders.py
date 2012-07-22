#!/usr/bin/env python

"""
Go through the seenOrders table, find all NOT IN that set for each region/type combo and delete
Greg Oberfield - gregoberfield@gmail.com
"""

import psycopg2
import time

# Turn on for standard output
TERM_OUT=False


def main():
    dbcon = psycopg2.connect("host=192.168.1.41 user=element43 host=192.168.1.41 password=element43")
    dbcon.autocommit = True

    curs = dbcon.cursor()
    
    # create and copy the data over
    sql = "DROP TABLE IF EXISTS market_data_seenordersworking"
    curs.execute(sql)
    sql = "CREATE TABLE market_data_seenordersworking (LIKE market_data_seenorders)"
    curs.execute(sql)
    sql = "INSERT INTO market_data_seenordersworking SELECT * FROM market_data_seenorders"
    curs.execute(sql)
    sql = "TRUNCATE market_data_seenorders"
    curs.execute(sql)
    loopsql = "SELECT * FROM market_data_seenordersworking ORDER BY type_id, region_id LIMIT 1"
    execute = True
    while (execute):
        curs.execute(loopsql)
        row = curs.fetchone()
        if row:
            regionID = row[1]
            typeID = row[2]
            sql = """INSERT INTO market_data_orderswarehouse (generated_at, region_id, type_id, price, order_range, id, is_bid, issue_date, duration, volume_entered, station_id, solar_system_id, uploader_ip_hash, message_key, is_suspicious) 
                     SELECT generated_at, region_id, type_id, price, order_range, id, is_bid, issue_date, duration, volume_entered, station_id, solar_system_id, uploader_ip_hash, message_key, is_suspicious FROM market_data_orders
                     WHERE type_id=%s AND region_id=%s AND market_data_orders.id NOT IN (SELECT id FROM market_data_seenordersworking WHERE type_id=%s AND region_id=%s)""" % (typeID, regionID, typeID, regionID)
            curs.execute(sql)
            sql = "DELETE FROM market_data_orders WHERE type_id=%s AND region_id=%s AND market_data_orders.id NOT IN (SELECT id FROM market_data_seenordersworking WHERE type_id=%s AND region_id=%s)" % (typeID, regionID, typeID, regionID)
            curs.execute(sql)
            if TERM_OUT==True:
                print "Type: ", typeID, " Region: ", regionID, " (affected: ", curs.rowcount, ")"
            sql = "DELETE FROM market_data_seenordersworking WHERE type_id=%s AND region_id=%s" % (typeID, regionID)
            curs.execute(sql)
        else:
            execute = False
    
if __name__ == '__main__':
    main()

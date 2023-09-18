#!/usr/bin/python3
"""
Script without a webpage interface that
only retrieves and displays the summed total result 
of all the polling units under any particular LGA
"""

import MySQLdb

#  MySQL database configuration settings based on my environment
db_config = {
        'host': "localhost",
        'db': "bincomphptest",
        'user': "root",
        'passwd': "root"
}

db = MySQLdb.connect(db_config)


#  Function to get summed total result for a LGA ordered by LGA id
def get_lga_result(lga_id):
    cursor = db.cursor()


    #  Query to get the summed total result for the selected LGA
    query = """
    SELECT party_name
    SUM(party_score)
    FROM announced_pu_results
    WHERE lga.id = {lga_id}
    GROUP BY party_name
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    return results


#  Function to get the list of LGAs
def get_lgas():
    cursor = db.cursor()


    #  Query to get the list of LGAs
    query = "SELECT lga_id, lga_name FROM lga"

    cursor.execute(query)
    lgas = cursor.fetchall()

    cursor.close()
    return lgas


#  Main function to print the summed total of results
def main():
    while true:
        print("Available LGAs:")
        lgas = get_lgas()
        for lga in lgas:
            print(f"{lga[0]}. {lga[1]}")

        try:
            lga_id int(input("Select an LGA by entering its ID (or any other key to exit): "))
        except valueError:
            break

        results = get_lga_result(lga_id)
        if results:
            print(f"Summed Total Result for LGA {lgas[lga_id - 1][1]}:")
            for row in results:
                print(f"{row[0]}: {row[1]}")


if __name__ == '__main__':
    main()

import logging
from config import database_uri
from config import database_schema
from config import database_table
from sqlalchemy import create_engine, text

# Set logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def get_authors_from_database(author_slug):
    """Connect to database and load commands into DataFrame."""
    engine = create_engine(database_uri, echo=True)
    # create a configured "Session" class
    # create a Session
    conn = engine.connect()
    sql = text('SELECT * from \"'
               + database_schema + '\".\"' + database_table
               + '\" WHERE slug = \'' + author_slug + '\';')
    results = conn.execute(sql)
    conn.close()
    dict_results = [dict(row) for row in results]
    print(dict_results)
    return dict_results

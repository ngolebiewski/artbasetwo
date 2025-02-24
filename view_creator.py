from sqlmodel import create_engine
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine
engine = create_engine(DATABASE_URL)

# SQL for the views
view_sql_1 = """
CREATE OR REPLACE VIEW mediums_by_artwork AS
SELECT string_agg("medium"."name", ', ') AS "mediums", 
       "artwork"."title", 
       "artwork"."id"
FROM "medium" 
JOIN "artworks_mediums" ON "medium"."id" = "artworks_mediums"."medium_id"
JOIN "artwork" ON "artworks_mediums"."artwork_id" = "artwork"."id"
GROUP BY "artwork"."id", "artwork"."title";
"""

view_sql_2 = """
CREATE OR REPLACE VIEW art_list AS
SELECT "artwork"."id", 
       first_name || ' ' || last_name AS "name", 
       "artwork"."title", 
       "artwork"."size", 
       "artwork"."year", 
       "mediums_by_artwork"."mediums", 
       "artwork"."image_url", 
       "artwork"."description", 
       "series"."name" AS "series", 
       "department"."name" AS "department", 
       "artwork"."price", 
       "artwork"."sold"
FROM "artwork"
JOIN "artist" ON "artist"."id" = "artwork"."artist_id"
JOIN "mediums_by_artwork" ON "mediums_by_artwork"."id" = "artwork"."id"
LEFT JOIN "series" ON "series"."id" = "artwork"."series_id"
LEFT JOIN "department" ON "department"."id" = "artwork"."department_id"
ORDER BY "artist"."last_name" ASC, "artwork"."id" ASC;
"""

# trigger_sql_1 = """
# CREATE OR REPLACE FUNCTION remove_artwork_from_mediums()
# RETURNS TRIGGER AS $$
# BEGIN
#     DELETE FROM artworks_mediums
#     WHERE artwork_id = OLD.id;
#     RETURN OLD;
# END;
# $$ LANGUAGE plpgsql;
# """

# trigger_sql_2 = """
# CREATE TRIGGER remove_artwork_from_mediums
# AFTER DELETE ON artwork
# FOR EACH ROW
# EXECUTE FUNCTION remove_artwork_from_mediums();
# """
    
# Execute the SQL to create views
with engine.connect() as connection:
    print("connected to", DATABASE_URL[:5], "...")
    connection.execute(text(view_sql_1))
    connection.execute(text(view_sql_2))
    print("Views created successfully!")
    # connection.execute(text(trigger_sql_1))
    # connection.execute(text(trigger_sql_2))
    # print("Trigers created successfully!")
    connection.commit()
    

print("Done!")


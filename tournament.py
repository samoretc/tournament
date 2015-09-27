#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try: 
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print "Error Connecting to Database"

def deleteMatches():
    """This function doesn't do anything, and isn't necessary based on my table design. 
    It is only included because it is called in tournament_test.py"""
    db, cursor = connect()
    cursor.execute("DELETE FROM matches")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM players")  
    db.commit()   
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    cursor.execute( " SELECT count(*) as num FROM players ")
    count = cursor.fetchone()[0]
    return int(count)

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    cursor.execute("INSERT INTO players (name, wins, matches) VALUES (%s, 0, 0)" , (name, ) )  
    db.commit()   
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    cursor.execute("SELECT id, name , wins, matches FROM players ORDER BY wins DESC")
    return cursor.fetchall() 

    #player = print row for row in cursor.fetchall() 
   # SELECT NAME From players Order by rank

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    cursor.execute("UPDATE players SET matches = matches + 1 WHERE id = %d or id = %d" % (winner, loser) );    
    db.commit()   
    cursor.execute("UPDATE players SET wins = wins + 1 WHERE id = %d" % (winner, ) )  
    db.commit()   
    cursor.execute("INSERT INTO matches (winner_id, loser_id ) VALUES ( %s, %s) ", (winner, loser))
    db.commit()
    db.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    
    This function works by executing the playerStandings function to get 
    list of standings, and then iterates over the
    list to find adjacent pairings. 
    """
    standings = playerStandings()
    pairings = []
    if (len(standings) % 2 != 0):
        return "Error, an evening number of players are supported"
    for i, player in enumerate(standings):
         if (i % 2 == 0):
              id1, name1 = player[0], player[1]
         else:
              pairings.append( (id1, name1, player[0], player[1] ) )
    return pairings



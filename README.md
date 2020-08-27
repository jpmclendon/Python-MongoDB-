# Python-MongoDB-
School project that was used to show me the interactions between Python language and the MongoDB software.
This program needs to have MongoDB installed and open before running, it also needs the required .csv files to inport to mongoDB. It isn't a code you can just run without proper set up, this is merely a example of integrating python and MongoDB to organize and get specific entrants to show up.

README:
  As soon as you begin the program, you will be asked to choose whcih query to use.
  Enter all values exactly as presented in this README file (case sensitive).
  Enter "q1" for the first query which takes a disease ID and shows all data related to it.
  Enter "q2" for the second query which shows drug-disease pairs and shows which gene up regulates or down regulates it.

  For query one, You will be asked to input Disease ID. Enter it exactly how it appears in the database for results.
  Example:
  Disease::DOID:263
  It will loop back around to beginning of the first query after you recieve the data. 

  For query two, You will be asked whether you want to input disease or a compound, enter "Disease" or "Compound", based on choice.
  After you choose, you will be asked to input the disease or compound id, exactly how it appears in the database.
  Example:
  Disease::DOID:784
  Compound::DB00887

  It will loop back around to the beginning of the second query after it prints the data.

  In order to change queries, you must exit the program and start it again.

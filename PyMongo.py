
import pymongo
from pymongo import MongoClient
Client = MongoClient()
db = Client.Hetio
posts = db.All

while True:
    User_Query = input('Please choose which query to use.Enter "q1" for the first query(Disease ID and all of its related information), and Enter "q2" for the second query(Drugs-Disease pairs).')

    if User_Query == "q1":
        file = open('C:\\nodes(text).txt', 'r')
        d = {}
        

        for line in file:
            x = line.split(',')
            s = x[0]
            n = x[1]
            k = x[2]
            d[s] = n,k
        while True:
            user = input('Please enter the Disease ID(Case sensitive)')
            
            print("The name and kind of " + user + " are " +str(d[user]))
            
            DiseaseCom = posts.find({'source':{'$regex':'^Compound'}, 'target':user}, {'_id':0, 'metaedge':0, 'target':0})
            for postcom in DiseaseCom:
                print(' The compounds that treat this disease are:' + str(postcom))
            DiseaseAna = posts.find({'source':user, 'target':{'$regex':'^Ana'}}, {'_id':0, 'metaedge':0, 'source':0})
            for postana in DiseaseAna:
                print('The parts of the anatomy that this disease effects are ' + str(postana))
            Gene_Count = posts.count_documents({'source':{'$regex':'^Gene'}, 'target':user})
            if Gene_Count != 0:
                DiseaseGene = posts.find({'source':{'$regex':'^Gene'}, 'target':user}, {'_id':0, 'metaedge':0, 'target':0})
                for postgene in DiseaseGene:
                    print('The genes that cause this disease are ' + str(postgene))
            if Gene_Count == 0:   
                print('There are no Genes that are the source of this Disease.')




    if User_Query == "q2":
        

        print("This query will show the user the raw data of specific compounds and the Diseases related to them, and vice versa.")
        while True:
            Choice = input('Please enter "Disease" or "Compound" to choose which to look for in the database(Case Sensitive):')
            
            if Choice == "Disease":
                Dis = input('Please enter the Disease ID(Case Sensitive):')
                disease_count = posts.count_documents({'source':Dis, 'target':{'$regex':'^Compound'}})
                disease_name = posts.find_one({'source':Dis, 'name':{'$exists':True}}, {'_id':0,'name':1})
                print('Disease:',disease_name)
                if disease_count != 0:
                    disease = posts.find({'source':Dis, 'target':{'$regex':'^Compound'}},{'_id':0, 'metaedge':0})
                    for post in disease:
                        print(post)
                    upreg_count = posts.count_documents({'source':Dis, 'metaedge':{'$regex':'^DuG'}})
                    if upreg_count != 0:
                        upreg = posts.find({'source':Dis, 'metaedge':{'$regex':'^DuG'}},{'_id':0, 'source':0})
                        for post in upreg:
                            print('This disease is upregulated by...', post)
                    downreg_count = posts.find({'source':Dis, 'metaedge':{'$regex':'^DdG'}})
                    if downreg_count != 0:
                        downreg = posts.find({'source':Dis, 'metaedge':{'$regex':'^DdG'}},{'_id':0, 'source':0})
                        for post in downreg:
                            print('This disease is downregulated by...', post)
                if disease_count == 0:
                    print('Since the database could not find compounds as targets for the specified disease, here is the disease as a target and the compounds as a source.')
                    disease2 = posts.find({'source':{'$regex':'^Compound'}, 'target':Dis}, {'_id':0, 'metaedge':0})
                    for post in disease2:
                        print(post)
                    upreg_count = posts.count_documents({'source':Dis, 'metaedge':{'$regex':'^DuG'}})
                    if upreg_count != 0:
                        upreg = posts.find({'source':Dis, 'metaedge':{'$regex':'^DuG'}},{'_id':0, 'source':0})
                        for post in upreg:
                            print('This disease is upregulated by...', post)
                    downreg_count = posts.find({'source':Dis, 'metaedge':{'$regex':'^DdG'}})
                    if downreg_count != 0:
                        downreg = posts.find({'source':Dis, 'metaedge':{'$regex':'^DdG'}},{'_id':0, 'source':0})
                        for post in downreg:
                            print('This disease is downregulated by...', post)
            

            if Choice == "Compound":
                Com = input('Please enter the compound ID(Case Sensitive):')
                compound_count = posts.count_documents({'source':Com , 'target':{'$regex':'^Disease'}})
                if compound_count != 0:
                    compound = posts.find({'source':Com, 'target':{'$regex':'^Disease'}}, {'_id':0, 'metaedge':0})
                    compound_name = posts.find_one({'source':Com, 'name':{'$exists':True}}, {'_id':0,'name':1})
                    print('Compound:',compound_name)
                    for post in compound:
                        print(post)
                    upreg_count = posts.count_documents({'source':Com, 'metaedge':{'$regex':'^CuG'}})
                    if upreg_count != 0:
                        upreg = posts.find({'source':Com, 'metaedge':{'$regex':'^CuG'}},{'_id':0, 'source':0})
                        for post in upreg:
                            print('This compound is upregulated by...', post)
                    downreg_count = posts.find({'source':Com, 'metaedge':{'$regex':'^CdG'}})
                    if downreg_count != 0:
                        downreg = posts.find({'source':Com, 'metaedge':{'$regex':'^CdG'}},{'_id':0, 'source':0})
                        for post in downreg:
                            print('This compound is downregulated by...', post)
                if compound_count == 0:
                    print('Since the database could not find diseases as targets for the specified compound, here is the compound as a target and the disease as the source.')
                    compound2 = posts.find({'source':{'$regex':'^Disease'}, 'target':Com },{'_id':0, 'metaedge':0})
                    for post in compound2:
                        print(post)
                    upreg_count = posts.count_documents({'source':Com, 'metaedge':{'$regex':'^CuG'}})
                    if upreg_count != 0:
                        upreg = posts.find({'source':Com, 'metaedge':{'$regex':'^CuG'}},{'_id':0, 'source':0})
                        for post in upreg:
                            print('This compound is upregulated by...', post)
                    downreg_count = posts.find({'source':Com, 'metaedge':{'$regex':'^CdG'}})
                    if downreg_count != 0:
                        downreg = posts.find({'source':Com, 'metaedge':{'$regex':'^CdG'}},{'_id':0, 'source':0})
                        for post in downreg:
                            print('This compound is downregulated by...', post)                                                                                              







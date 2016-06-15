"""
PRAISE THE SUN

Author: William Pereira

For Python ver: 2.7

////////'mold' cheat sheet:

1 - ProductType
"""
from neo4j.v1 import GraphDatabase, basic_auth

def connectDB():
	driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "admin"))
	session = driver.session()	
	return session

session = connectDB()

subclassof = ""

with open('data_100.ttl','r', buffering = 4096) as f1:
	print ("--------------File successfully loaded.--------------")
	for line in f1:
		if('    ' in line):
#######################################################################################################			
			if(mold = 1): 
				if('rdf:type' in line):
					pass
				elif('rdfs:label' in line):
					label = line.replace("rdfs:label ","")
					label = line.replace(" ;","")
				elif('rdfs:subClassOf' in line):
					subclassof = line.replace("rdfs:subClassOf bsbm-inst:","")
					subclassof = line.replace(" ;","")
				elif('rdfs:comment' in line):
					comment = line.replace("rdfs:comment ","")
					comment = line.replace(" ;","")
				elif('dc:publisher' in line):
					publisher = line.replace("dc:publisher <","")
					publisher = line.replace("> ;","")
				elif('dc:date' in line):
					date = line.replace("dc:date ","")
					date = line.replace("^^xsd:date .","")
					# QUERY
					session.run("CREATE ("+header+":ProductType {header:\""+header+"\",label:"+label+",comment:"+comment+",date:"+date+"})")
					if(subclassof == ""):
						session.run("CREATE (publisher:Publisher {header:\""+publisher+"\"})")
					else:
						session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+subclassof+"\"}) CREATE son-[:subClassOf]->father")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE son-[:publisher]->father")
				else:
					print("Well, this is embarrassing... mold="+mold)
#######################################################################################################			
										
		else:
			if('bsbm-inst:ProductType' in line):
				header = line.replace("bsbm-inst:","")
				mold = 1

session.close()
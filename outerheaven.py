"""
PRAISE THE SUN

Author: William Pereira

For Python ver: 2.7

////////'mold' cheat sheet:

0  - exit
1  - ProductType
2  - ProductFeature
3  - Producer
4  - Product
"""
from neo4j.v1 import GraphDatabase, basic_auth
import time

def timer(start_time):
	start_time = 0
	print("--- %s seconds ---" %(time.time() - start_time))
	print("--- or ---")
	while (True):
		if(start_time>=60):
			minute_time = minute_time + 1
			start_time = start_time - 60
		else:
			False
	print("--- "+minute_time+" minutes and "+start_time+" seconds ---")
		
def checkCountry(country,listCountry):
	for i in listCountry:
		if(country == str(i)): 
			return (listCountry,True)
	listCountry.append(country)
	return (listCountry,False)

def connectDB():
	driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "admin"))
	session = driver.session()	
	return session

session = connectDB()

# PERTINENT VARIABLES
# start_time = time.time() NEEDS REVIEW
subclassof = ""
listCountry = []

# PROGRAM
with open('data_100.ttl','r', buffering = 4096) as f1:
	print ("--------------File successfully loaded.--------------")
	for line in f1:
		if('    ' in line):
#######################################################################################################			
			if(mold == 1):
				pass
				if('rdf:type' in line):
					pass
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label \"","")
					label = label.replace("\" ;","")
					# print(label)
				elif('rdfs:subClassOf' in line):
					subclassof = line.replace("    rdfs:subClassOf bsbm-inst:","")
					subclassof = subclassof.replace(" ;","")
					# print(subclassof)
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
				elif('dc:publisher' in line):
					publisher = line.replace("    dc:publisher <","")
					publisher = publisher.replace("> ;","")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					# QUERY
					session.run("CREATE ("+header+":ProductType {header:\""+header+"\",label:\""+label+"\",comment:"+comment+",date:"+date+"})")
					if(subclassof == ""):
						session.run("CREATE (publisher:Publisher {header:\""+publisher+"\"})")
					else:
						session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+subclassof+"\"}) CREATE (son)-[:subClassOf]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 2):
				pass
				if('rdf:type' in line):
					pass
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
					# print(label)
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
				elif('dc:publisher' in line):
					pass
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					# QUERY
					session.run("CREATE ("+header+":ProductFeature {header:\""+header+"\",label:"+label+",comment:"+comment+",date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")

				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 3):
				if('rdf:type' in line):
					pass
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
				elif('foaf:homepage' in line):
					homepage = line.replace("    foaf:homepage <","")
					homepage = homepage.replace("> ;","")
				elif('bsbm:country' in line):
					country = line.replace("    bsbm:country <","")
					country = country.replace("> ;","")
				elif('dc:publisher' in line):
					pass
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					# QUERY
					session.run("CREATE ("+header+":Producer {header:\""+header+"\",label:"+label+",comment:"+comment+",date:"+date+"})")
					session.run("CREATE (homepage:Homepage {header:\""+homepage+"\"})")
					listCountry,countryChecked=checkCountry(country,listCountry)
					if(countryChecked == False):
						session.run("CREATE (country:Country {header:\""+country+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+homepage+"\"}) CREATE (son)-[:homepage]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+country+"\"}) CREATE (son)-[:country]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 4):
				pass
				# print("bom dia!")
#######################################################################################################			
			else:
				print ("--------------Executing database querys.--------------")
				session.close()
				# timer(start_time) NEEDS REVIEW 
				print ("--------------Closing program.--------------")
				print (exit)
				input()
#######################################################################################################			
										
		else:
			if('bsbm-inst:ProductType' in line):
				header = line.replace("bsbm-inst:","")
				mold = 1
			elif('bsbm-inst:ProductFeature' in line):
				header = line.replace("bsbm-inst:","")
				mold = 2
			elif('dataFromProducer' in line):
				if(':Producer' in line):
					header = line.split(':')[1]
					mold = 3
				else:
					mold = 4
			else:
				mold = 0

session.close()
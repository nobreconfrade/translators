"""
PRAISE THE SUN

Author: William Pereira

For Python ver: 2.7

to add in the database:MATCH p=(header:Product)-[]->() RETURN p LIMIT 100

////////'mold' cheat sheet:

0  - exit
1  - ProductType
2  - ProductFeature
3  - Producer
4  - Product
"""
from neo4j.v1 import GraphDatabase, basic_auth
from timeit import default_timer as timer
import sys

def connectDB():
	driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "admin"))
	session = driver.session()	
	return session

def timeCount(startTimer):
	minuteTime = 0
	endTimer = timer() - startTimer 
	print("--- "+str(endTimer)+" seconds ---")
	print("--- or ---")
	while (endTimer>=60):
		minuteTime = minuteTime + 1
		endTimer = endTimer - 60
	print("--- "+str(minuteTime)+" minutes and "+str(endTimer)+" seconds ---")
		
def checkCountry(country,listCountry):
	for i in listCountry:
		if(country == str(i)): 
			return (listCountry,True)
	listCountry.append(country)
	return (listCountry,False)

def getProductPropertyNumeric(line):
	propertynumeric = line.split(' ')[4]
	propertynumeric = propertynumeric.replace('bsbm:','')
	numeric = line.split(' ')[5]
	# print ("-----------------------------------")
	# print numeric
	numeric = numeric.replace('^^xsd:integer','')
	# print numeric
	stringpropertynumeric = propertynumeric+":"+numeric
	return stringpropertynumeric

def getProductPropertyTextural(line):
	propertytextual = line.split(' ')[4]
	propertytextual = propertytextual.replace('bsbm:','')
	textual = line.replace('bsbm:'+propertytextual+' ','')
	textual = textual.replace('^^xsd:string ;','')
	# print textual
	stringpropertytextual = propertytextual+":"+textual
	return stringpropertytextual

# PERTINENT VARIABLES
session = connectDB()
startTimer = timer()
subclassof = ""
listCountry = []

# PROGRAM
with open(sys.argv[1],'r', buffering = 4096) as f1:
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
				###########BE AWARE###########
				# I still don't know if the 4 spaces in the beggining of every line is going to cause trouble with the split(' ')
				###########BE AWARE###########
				if('rdf:type bsbm:Product' in line):
					listpropertynumeric = []
					listpropertytextual = []
					listproductfeature = []
					pass
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
				elif('rdf:type bsbm-inst' in line):
					producttype = line.split(':')[2]
					producttype = producttype.replace(" ;","")
				elif('bsbm:productPropertyNumeric' in line):
					listpropertynumeric.append(getProductPropertyNumeric(line)) 
				elif('bsbm:productPropertyTextual' in line):
					listpropertytextual.append(getProductPropertyTextural(line))
				elif('bsbm:productFeature' in line):
					productfeature = line.split(':')[2]
					productfeature = productfeature.replace(" ;","")
					listproductfeature.append(productfeature)
				elif('bsbm:producer' in line):
					producer = line.split(':')[2]
					producer = producer.replace(" ;","")
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					# QUERY
					# print listpropertynumeric
					outputnumeric = ','.join(listpropertynumeric)
					# print outputnumeric
					outputtextual = ','.join(listpropertytextual)
					session.run("CREATE ("+header+":Product {header:\""+header+"\",label:"+label+",comment:"+comment+","+outputnumeric+","+outputtextual+",date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+producer+"\"}) CREATE (son)-[:producer]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+producttype+"\"}) CREATE (son)-[:producttype]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
					for e in listproductfeature:
						session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+e+"\"}) CREATE (son)-[:productfeature]->(father)")

				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			else:
				print ("--------------Executing database querys.--------------")
				session.close()
				timeCount(startTimer)
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
					header = line.split(':')[1]
					mold = 4
			else:
				mold = 0

session.close()
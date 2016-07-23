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
5  - Vendor
6  - Offer
7  - Reviewer
8  - Review
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

# PERTINENT VARIABLES
session = connectDB()
startTimer = timer()
subclassof = ""

# PROGRAM
with open(sys.argv[1],'r', buffering = 4096) as f1:
	print ("--------------File successfully loaded.--------------")
	for line in f1:
		if('    ' in line):
#######################################################################################################			
			if(mold == 1):
				if('rdf:type' in line):
					pass
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
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
					session.run("CREATE ("+header+":ProductType {header:\""+header+"\"})")
					session.run("CREATE ("+header+":label {label:"+label+"})")
					session.run("CREATE ("+header+":comment {comment:"+comment+"})")
					session.run("CREATE ("+header+":date {date:"+date+"})")
					if(subclassof == ""):
						session.run("CREATE (publisher:Publisher {publisher:\""+publisher+"\"})")
					else:
						session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+subclassof+"\"}) CREATE (son)-[:subClassOf]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{label:"+label+"}) CREATE (son)-[:label]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{comment:"+comment+"}) CREATE (son)-[:comment]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{publisher:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 2):
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
			elif(mold == 5):
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
					session.run("CREATE ("+header+":Vendor {header:\""+header+"\",label:"+label+",comment:"+comment+",date:"+date+"})")
					session.run("CREATE (homepage:Homepage {header:\""+homepage+"\"})")
					listCountry,countryChecked=checkCountry(country,listCountry)
					if(countryChecked == False):
						session.run("CREATE (country:Country {header:\""+country+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+homepage+"\"}) CREATE (son)-[:homepage]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+country+"\"}) CREATE (son)-[:country]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 6):
				if('rdf:type' in line):
					pass
				elif('bsbm:product' in line):
					product = line.split(':')[2]
					product = product.replace(" ;","")
				elif('bsbm:vendor' in line):
					vendor = line.split(':')[2]
					vendor = vendor.replace(" ;","")
				elif('bsbm:price' in line):
					price = line.replace("    bsbm:price ","")
					price = price.replace("^^bsbm:USD ;","")
				elif('bsbm:validFrom' in line):
					validfrom = line.replace("    bsbm:validFrom ","")
					validfrom = validfrom.replace("^^xsd:dateTime ;","")
				elif('bsbm:validTo' in line):
					validto = line.replace("    bsbm:validTo ","")
					validto = validto.replace("^^xsd:dateTime ;","")
				elif('bsbm:deliveryDays' in line):
					deliverydays = line.replace("    bsbm:deliveryDays ","")
					deliverydays = deliverydays.replace("^^xsd:integer ;","")
				elif('bsbm:offerWebpage' in line):
					offerwebpage = line.replace("bsbm:offerWebpage <","")
					offerwebpage = offerwebpage.replace("> ;","")
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					# QUERY
					session.run("CREATE ("+header+":Offer {header:\""+header+"\",price:"+price+",validFrom:"+validfrom+",validTo:"+validto+",deliveryDays:"+deliverydays+",date:"+date+"})")
					session.run("CREATE (offerwebpage:OfferWebpage {header:\""+offerwebpage+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+product+"\"}) CREATE (son)-[:product]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+vendor+"\"}) CREATE (son)-[:vendor]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+offerwebpage+"\"}) CREATE (son)-[:offerwebpage]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 7):
				if('rdf:type' in line):
					pass
				elif('foaf:name' in line):
					name = line.replace("    foaf:name ","")
					name = name.replace(" ;","")
				elif('foaf:mbox_sha1sum' in line):
					mbox = line.replace("    foaf:mbox_sha1sum ","")
					mbox = mbox.replace(" ;","")
				elif('bsbm:country' in line):
					country = line.replace("    bsbm:country <","")
					country = country.replace("> ;","")					
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					# QUERY
					session.run("CREATE ("+header+":Person {header:\""+header+"\",name:"+name+",mbox_sha1sum:"+mbox+",date:"+date+"})")
					listCountry,countryChecked=checkCountry(country,listCountry)
					if(countryChecked == False):
						session.run("CREATE (country:Country {header:\""+country+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+country+"\"}) CREATE (son)-[:country]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 8):
				if('rdf:type' in line):
					listrating = []
					pass
				elif('bsbm:reviewFor' in line):
					reviewfor = line.split(':')[2]
					reviewfor = reviewfor.replace(" ;","")
				elif('rev:reviewer' in line):
					reviewer = line.split(':')[2]
					reviewer = reviewer.replace(" ;","")
				elif('dc:title' in line):
					title = line.replace("    dc:title ","")
					title = title.replace(" ;","")
				elif('rev:text' in line):
					text = line.split('@')[0]
					text = text.replace("    rev:text ","")
				elif('bsbm:rating' in line):
					listrating.append(getRating(line))
				elif('bsbm:reviewDate' in line):
					reviewdate = line.replace("    bsbm:reviewDate ","")
					reviewdate = reviewdate.replace("^^xsd:dateTime ;","")
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					# QUERY
					outputrating = ','.join(listrating)
					if(len(outputrating)==0):
						session.run("CREATE ("+header+":Review {header:\""+header+"\",title:"+title+",text:"+text+",reviewDate:"+reviewdate+",date:"+date+"})")
					else:
						session.run("CREATE ("+header+":Review {header:\""+header+"\",title:"+title+",text:"+text+","+outputrating+",reviewDate:"+reviewdate+",date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+reviewfor+"\"}) CREATE (son)-[:reviewfor]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+reviewer+"\"}) CREATE (son)-[:reviewer]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
#######################################################################################################			
			else:
				pass
#######################################################################################################			
		else:
			if('bsbm-inst:ProductType' in line):
				header = line.replace("bsbm-inst:","")
				mold = 1
			# elif('bsbm-inst:ProductFeature' in line):
			# 	header = line.replace("bsbm-inst:","")
			# 	mold = 2
			# elif('dataFromProducer' in line):
			# 	if(':Producer' in line):
			# 		header = line.split(':')[1]
			# 		mold = 3
			# 	else:
			# 		header = line.split(':')[1]
			# 		mold = 4
			# elif('dataFromVendor' in line):
			# 	if (':Vendor' in line):
			# 		header = line.split(':')[1]
			# 		mold = 5
			# 	else:
			# 		header = line.split(':')[1]
			# 		mold = 6
			# elif('dataFromRatingSite' in line):
			# 	if (':Reviewer' in line):
			# 		header = line.split(':')[1]
			# 		mold = 7
			# 	else:
			# 		header = line.split(':')[1]
			# 		mold = 8
			else:
				mold = 0

print ("--------------Executing database querys.--------------")
session.close()
timeCount(startTimer)
print ("--------------Closing program.--------------")
print (exit)
input()
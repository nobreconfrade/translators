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

def checkVariable(variable,lists):
	for i in lists:
		if(variable == str(i)): 
			return (lists,True)
	lists.append(variable)
	return (lists,False)

def connectDB():
	driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "admin"))
	session = driver.session()	
	return session

def timeCount(starttimer):
	minuteTime = 0
	endTimer = timer() - starttimer 
	print("--- "+str(endTimer)+" seconds ---")
	print("--- or ---")
	while (endTimer>=60):
		minuteTime = minuteTime + 1
		endTimer = endTimer - 60
	print("--- "+str(minuteTime)+" minutes and "+str(endTimer)+" seconds ---")

# PERTINENT VARIABLES
session = connectDB()
starttimer = timer()
subclassof = ""
listcountry = []
listdate = []
listnumeric = []
listdatetime = []
flag = 0

# PROGRAM
with open(sys.argv[1],'r', buffering = 4096) as f1:
	print ("--------------File successfully loaded.--------------")
	for line in f1:
		if('    ' in line):
#######################################################################################################			
			if(mold == 1):
				if('rdf:type' in line):
					session.run("CREATE ("+header+":ProductType {header:\""+header+"\"})")
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+label+"})")
					# print(label)
				elif('rdfs:subClassOf' in line):
					subclassof = line.replace("    rdfs:subClassOf bsbm-inst:","")
					subclassof = subclassof.replace(" ;","")
					# print(subclassof)
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+comment+"})")
				elif('dc:publisher' in line):
					publisher = line.replace("    dc:publisher <","")
					publisher = publisher.replace("> ;","")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					listdate,dateChecked=checkVariable(date,listdate)
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					if(subclassof == ""):
						session.run("CREATE (string:string {string:\""+publisher+"\"})")
					else:
						session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+subclassof+"\"}) CREATE (son)-[:subClassOf]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+label+"}) CREATE (son)-[:label]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+comment+"}) CREATE (son)-[:comment]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 2):
				if('rdf:type' in line):
					session.run("CREATE ("+header+":ProductFeature {header:\""+header+"\"})")
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+label+"})")
					# print(label)
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+comment+"})")
				elif('dc:publisher' in line):
					session.run("MATCH (son{header:\""+header+"\"}),(father{publisher:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					listdate,dateChecked=checkVariable(date,listdate)
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+label+"}) CREATE (son)-[:label]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+comment+"}) CREATE (son)-[:comment]->(father)")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 3):
				if('rdf:type' in line):
					session.run("CREATE ("+header+":Producer {header:\""+header+"\"})")
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+label+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+label+"}) CREATE (son)-[:label]->(father)")
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+comment+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+comment+"}) CREATE (son)-[:comment]->(father)")
				elif('foaf:homepage' in line):
					homepage = line.replace("    foaf:homepage <","")
					homepage = homepage.replace("> ;","")
					session.run("CREATE (homepage:string {string:\""+homepage+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+homepage+"\"}) CREATE (son)-[:homepage]->(father)")
				elif('bsbm:country' in line):
					country = line.replace("    bsbm:country <","")
					country = country.replace("> ;","")
					listcountry,countryChecked=checkVariable(country,listcountry)
					if(countryChecked == False):
						session.run("CREATE (country:string {string:\""+country+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+country+"\"}) CREATE (son)-[:country]->(father)")
				elif('dc:publisher' in line):
					pass
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					listdate,dateChecked=checkVariable(date,listdate)
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 4):
				if('rdf:type bsbm:Product' in line):
					session.run("CREATE ("+header+":Product {header:\""+header+"\"})")
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+label+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+label+"}) CREATE (son)-[:label]->(father)")
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+comment+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+comment+"}) CREATE (son)-[:comment]->(father)")
				elif('rdf:type bsbm-inst' in line):
					producttype = line.split(':')[2]
					producttype = producttype.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+producttype+"\"}) CREATE (son)-[:producttype]->(father)")
				elif('bsbm:productPropertyNumeric' in line):
					propertynumeric = line.split(' ')[4]
					propertynumeric = propertynumeric.replace('bsbm:','')
					numeric = line.split(' ')[5]
					numeric = numeric.replace('^^xsd:integer','')
					listnumeric,numericChecked=checkVariable(numeric,listnumeric)
					if(numericChecked == False):
						session.run("CREATE ("+header+":integer {integer:"+numeric+"})")
						# print (numeric)
					session.run("MATCH (son{header:\""+header+"\"}),(father{integer:"+numeric+"}) CREATE (son)-[:"+propertynumeric+"]->(father)")
				elif('bsbm:productPropertyTextual' in line):
					propertytextual = line.split(' ')[4]
					propertytextual = propertytextual.replace('bsbm:','')
					textual = line.replace('    bsbm:'+propertytextual+' ','')
					textual = textual.replace('^^xsd:string ;','')
					session.run("CREATE ("+header+":string {string:"+textual+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+textual+"}) CREATE (son)-[:"+propertytextual+"]->(father)")
				elif('bsbm:productFeature' in line):
					productfeature = line.split(':')[2]
					productfeature = productfeature.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+productfeature+"\"}) CREATE (son)-[:productfeature]->(father)")
				elif('bsbm:producer' in line):
					producer = line.split(':')[2]
					producer = producer.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+producer+"\"}) CREATE (son)-[:producer]->(father)")
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					listdate,dateChecked=checkVariable(date,listdate)
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 5):
				if('rdf:type' in line):
					session.run("CREATE ("+header+":Vendor {header:\""+header+"\"})")
				elif('rdfs:label' in line):
					label = line.replace("    rdfs:label ","")
					label = label.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+label+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+label+"}) CREATE (son)-[:label]->(father)")
				elif('rdfs:comment' in line):
					comment = line.replace("    rdfs:comment ","")
					comment = comment.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+comment+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+comment+"}) CREATE (son)-[:comment]->(father)")
				elif('foaf:homepage' in line):
					homepage = line.replace("    foaf:homepage <","")
					homepage = homepage.replace("> ;","")
					session.run("CREATE (homepage:string {string:\""+homepage+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+homepage+"\"}) CREATE (son)-[:homepage]->(father)")
				elif('bsbm:country' in line):
					country = line.replace("    bsbm:country <","")
					country = country.replace("> ;","")
					listcountry,countryChecked=checkVariable(country,listcountry)
					if(countryChecked == False):
						session.run("CREATE (country:string {string:\""+country+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+country+"\"}) CREATE (son)-[:country]->(father)")
				elif('dc:publisher' in line):
					pass
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					listdate,dateChecked=checkVariable(date,listdate)
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 6):
				if('rdf:type' in line):
					session.run("CREATE ("+header+":Offer {header:\""+header+"\"})")
				elif('bsbm:product' in line):
					product = line.split(':')[2]
					product = product.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+product+"\"}) CREATE (son)-[:product]->(father)")
				elif('bsbm:vendor' in line):
					vendor = line.split(':')[2]
					vendor = vendor.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+vendor+"\"}) CREATE (son)-[:vendor]->(father)")
				elif('bsbm:price' in line):
					price = line.replace("    bsbm:price ","")
					price = price.replace("^^bsbm:USD ;","")
					session.run("CREATE ("+header+":float {float:"+price+"})")
				elif('bsbm:validFrom' in line):
					validfrom = line.replace("    bsbm:validFrom ","")
					validfrom = validfrom.replace("^^xsd:dateTime ;","")
					listdatetime,datetimeChecked=checkVariable(validfrom,listdatetime)
					if(datetimeChecked == False):
						session.run("CREATE ("+header+":datetime {datetime:"+validfrom+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{datetime:"+validfrom+"}) CREATE (son)-[:validfrom]->(father)")
				elif('bsbm:validTo' in line):
					validto = line.replace("    bsbm:validTo ","")
					validto = validto.replace("^^xsd:dateTime ;","")
					listdatetime,datetimeChecked=checkVariable(validto,listdatetime)
					if(datetimeChecked == False):
						session.run("CREATE ("+header+":datetime {datetime:"+validto+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{datetime:"+validto+"}) CREATE (son)-[:validto]->(father)")
				elif('bsbm:deliveryDays' in line):
					deliverydays = line.split(' ')[5]
					deliverydays = deliverydays.replace('^^xsd:integer','')
					listnumeric,numericChecked=checkVariable(deliverydays,listnumeric)
					if(numericChecked == False):
						session.run("CREATE ("+header+":integer {integer:"+deliverydays+"})")
						# print(deliverydays)
					session.run("MATCH (son{header:\""+header+"\"}),(father{integer:"+deliverydays+"}) CREATE (son)-[:deliverydays]->(father)")
				elif('bsbm:offerWebpage' in line):
					offerwebpage = line.replace("bsbm:offerWebpage <","")
					offerwebpage = offerwebpage.replace("> ;","")
					session.run("CREATE (offerwebpage:OfferWebpage {header:\""+offerwebpage+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+offerwebpage+"\"}) CREATE (son)-[:offerwebpage]->(father)")
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					listdate,dateChecked=checkVariable(date,listdate)
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")				
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 7):
				if('rdf:type' in line):
					session.run("CREATE ("+header+":Person {header:\""+header+"\"})")
				elif('foaf:name' in line):
					name = line.replace("    foaf:name ","")
					name = name.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+name+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+name+"}) CREATE (son)-[:name]->(father)")
				elif('foaf:mbox_sha1sum' in line):
					mbox = line.replace("    foaf:mbox_sha1sum ","")
					mbox = mbox.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+mbox+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+mbox+"}) CREATE (son)-[:mbox_sha1sum]->(father)")
				elif('bsbm:country' in line):
					country = line.replace("    bsbm:country <","")
					country = country.replace("> ;","")			
					listcountry,countryChecked=checkVariable(country,listcountry)
					if(countryChecked == False):
						session.run("CREATE (country:string {string:\""+country+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+country+"\"}) CREATE (son)-[:country]->(father)")		
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
					flag = flag + 1
					if (flag == 1):
						session.run("CREATE ("+header+":string {string:\""+publisher+"\"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					listdate,dateChecked=checkVariable(date,listdate)
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			elif(mold == 8):
				if('rdf:type' in line):
					session.run("CREATE ("+header+":Review {header:\""+header+"\"})")
				elif('bsbm:reviewFor' in line):
					reviewfor = line.split(':')[2]
					reviewfor = reviewfor.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+reviewfor+"\"}) CREATE (son)-[:reviewfor]->(father)")
				elif('rev:reviewer' in line):
					reviewer = line.split(':')[2]
					reviewer = reviewer.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{header:\""+reviewer+"\"}) CREATE (son)-[:reviewer]->(father)")
				elif('dc:title' in line):
					title = line.replace("    dc:title ","")
					title = title.replace(" ;","")
					session.run("CREATE ("+header+":string {string:"+title+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+title+"}) CREATE (son)-[:title]->(father)")
				elif('rev:text' in line):
					text = line.split('@')[0]
					text = text.replace("    rev:text ","")
					session.run("CREATE ("+header+":string {string:"+text+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:"+text+"}) CREATE (son)-[:text]->(father)")
				elif('bsbm:rating' in line):
					rating = line.split(' ')[4]
					rating = rating.replace('bsbm:','')
					value = line.split(' ')[5]
					value = value.replace('^^xsd:integer','')
					listnumeric,numericChecked=checkVariable(value,listnumeric)
					if(numericChecked == False):
						session.run("CREATE ("+header+":integer {integer:"+value+"})")
						# print (value)
					session.run("MATCH (son{header:\""+header+"\"}),(father{integer:"+value+"}) CREATE (son)-[:"+rating+"]->(father)")
				elif('bsbm:reviewDate' in line):
					reviewdate = line.replace("    bsbm:reviewDate ","")
					reviewdate = reviewdate.replace("^^xsd:dateTime ;","")
					listdatetime,datetimeChecked=checkVariable(reviewdate,listdatetime)
					if(datetimeChecked == False):
						session.run("CREATE ("+header+":datetime {datetime:"+reviewdate+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{datetime:"+reviewdate+"}) CREATE (son)-[:reviewdate]->(father)")
				elif('dc:publisher' in line):
					publisher = line.split(':')[2]
					publisher = publisher.replace(" ;","")
					session.run("MATCH (son{header:\""+header+"\"}),(father{string:\""+publisher+"\"}) CREATE (son)-[:publisher]->(father)")
				elif('dc:date' in line):
					date = line.replace("    dc:date ","")
					date = date.replace("^^xsd:date .","")
					if(dateChecked == False):
						session.run("CREATE ("+header+":date {date:"+date+"})")
					session.run("MATCH (son{header:\""+header+"\"}),(father{date:"+date+"}) CREATE (son)-[:date]->(father)")
				else:
					print("Well, this is embarrassing... mold="+str(mold))
#######################################################################################################			
			else:
				print ("i don't know =/")
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
			elif('dataFromVendor' in line):
				if (':Vendor' in line):
					header = line.split(':')[1]
					mold = 5
				else:
					header = line.split(':')[1]
					mold = 6
			elif('dataFromRatingSite' in line):
				if (':Reviewer' in line):
					header = line.split(':')[1]
					mold = 7
				else:
					header = line.split(':')[1]
					mold = 8
			else:
				mold = 0

print ("--------------Executing database querys.--------------")
session.close()
timeCount(starttimer)
print ("--------------Closing program.--------------")
print (exit)
input()
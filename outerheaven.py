"""
PRAISE THE SUN

Author: William Pereira

For Python ver: 2.7

"""
from neo4j.v1 import GraphDatabase, basic_auth

def connectDB():
	driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "admin"))
	session = driver.session()	
	return session

session = connectDB()

producer = "producer1"
label = "desensitizations bleachers gentries"	
datex = "2003-06-15"
comment = "journalism tramroads chemoreceptive pipets wordless accumulated finches grazed packers eggbeater feebler epileptoid monadism sickened vexes mensas marimbas christianizing leary snowbound"

session.run("CREATE ({producer}:Producer {label:{label},datex:{datex},comment:{comment}})",{"producer":producer,"label":label,"datex":datex,"comment":comment})

product = "product1"
label = "turgescence retrospection"	
datex = "2000-11-01"
comment = "attaining requirement legitimately overfatigue blancmange pedestrians druidisms commonwealths woofs hippie muddled livest upstages entourages denominations agrees salves perched theatergoers rigorists nae archimandrite cherty bingos hobnobbed praxeological parsable tetralogy imputers altruisms erecters assegais insinuator overwhelming homemaker conjunctiva filespec adaptability ionizes monogrammed moisteners unburdening walkings invocations riffled salaaming pedantically footworn semplice potholders flasks loopholes actually gushes coworkers cheapening beadroll immensely sibilance ombres stifling extremists"
propertyNumeric1 = "831"
propertyNumeric2 = "312"
propertyNumeric3 = "735"
propertyText1 = "nontenure declined grubs graybacks barmiest reflective flinching staffs spieler pittance underlips gainsays subcompact"
propertyText2 = "anymore alternation alchemies unplugs almshouses obdurately cattish triskaidekaphobe heroics"
propertyText3 = "tempers addresses sprinklers disabuses posterities phosgenes evacuation gaudies downer appeared quadrics disguisements fatalism"

session.run("CREATE ({product}:Product {label:{label},datex:{datex},comment:{comment},propertyNumeric1:{propertyNumeric1},"
"propertyNumeric2:{propertyNumeric2},propertyNumeric3:{propertyNumeric3},propertyText1:{propertyText1},"
"propertyText2:{propertyText2},propertyText3:{propertyText3}})", {"product":product,"label":label,"datex": datex, "comment":comment,
"propertyNumeric1":propertyNumeric1, "propertyNumeric2":propertyNumeric2, "propertyNumeric3":propertyNumeric3,
"propertyText1":propertyText1, "propertyText2":propertyText2, "propertyText3":propertyText3}) 

relation = "bsbm:producer"

session.run("CREATE ("product") -[:"relation"]->("producer")") #FIX THIS LINE LIKE 36 AND 23

# result = session.run("MATCH (a:Person) WHERE a.name = 'Arthur' RETURN a.name AS name, a.title AS title")
# for record in result:
# 	print("%s %s" % (record["title"], record["name"]))
session.close()
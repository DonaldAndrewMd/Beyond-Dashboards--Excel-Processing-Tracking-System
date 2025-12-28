#The script below should generate the exact data type I have
import pandas as pd
import numpy as np

num_users = 10000
np.random.seed(42)  
# The array of names below were retrieved from: https://studentsoftheworld.info/penpals/stats.php?Pays=NIG
fnames = ['favour','Esther','Blessing','precious','Joy','DIVINE','Ayomide','Jessica','Sharon','mercy','Anu','chinonso','chinelo','Queen','Jennifer','Waajidah','Zita','Margaret','Rachael','kiara','Treasure','Mary','olabisi','kebe','rosemary','Grace','zainab','oreoluwa','Redeem','Hellen','dorcas','Diana','Kelechi','stella','Rose','Anie','stephanie','Chiamaka','Adaeze','Victoria','Pollyanna','Blossom','sophia','Temitope','Ashley','Iyanuoluwa','katrine','Patricia','anna','Marie','Gabriel','benita','ajigbotoso','Gloria','Justin','Enny','Amala','Tife','Patience','Vika','Maryjane','Debby','marisha','Alma','prudent','Joyce','Anny','Yogamama','Bella','vanessa','Laye','Jasmine','Weneydarl','MinRee','Loveth','Rita','Ummu','Kel','Oputa','racheal','Bethel','Gem','Doria','Kaothara','Chidera','Michelle','Taiwo','Cleo','AMANDA','Omotolani','joycey','Ashimedua','William','Gemma','Abisoye','owoeye','lylian','Diepreye','velma','melody','Emmanuel','Michael','samuel','Victor','DANIEL','David','Peter','Isaac','Sam','paul','Joseph','Israel','Charles','Williams','Kingsley','kelvin','gabriel','vincent','SOLOMON','IDRIS','azeez','Richard','George','Prince','John','stephen','Alex','Walter','Raphael','Francis','Joel','Jude','Goodluck','Micheal','chidi','Pascal','Shalom','sodiq','Adewale','Muhammed','Adeyemi','Ayobami','zion','jeffrey','oyekunle','victory','Chukwuka','joy','Ekele','ejike james','kristos','Young','Prosper','Jonathan','Wales','Daniel Scott','Oluwashola','sheriff','Mavis','Ub','Toheeb','Bezaleel','Alin','Noxy','Chinenerem','amara','icety','Sylvester','bolaji','Misan','Etido','max','Elijah','Colade','Divon','Okwuchukwu','Jibrin','AUWAL','Fisayo','olaolu','monday','Gideon','timmy','ikeora mark ekene','Henry jack','Oni','rex','Kofi','kizito','Umar','JAKE','mofe','ceaser','Tini','kenny','Ahmad','Ola','James','Kester','Oscar']
lnames=['Adeoye','Adebayo','Ogunleye','Adewale','Olawale','Akinlade','Ogunyemi','Akinyemi','Ojo','Akinola','Okoro','Balogun','Okeke','Bello','Okafor','Danladi','Olaleye','Eze','Olatunji','Fashola','Owolabi','Ibrahim','Oyedele','Idris','Afolabi','Ige','Aina','Jimoh','Ajayi','Kareem','Alabi','Lawal','Aluko','Makanjuola','Momoh','Nwankwo','Nwachukwu','Obi','Nwosu','Odeyemi','Onyemaechi','Ogunbiyi','Osagie','Olufemi','Salami','Olusola','Sodiq','Olutayo','Taiwo','Owolabi','Tijani','Popoola','Umaru','Raji','Usman','Suleiman','Yusuf','Yakubu','Akinyemi','Abiodun','Akinlade','Abiola','Akinola','Adedayo','Akinyemi','Adekunle','Ogunleye','Adeola','Olawale','Adeyemi','Okoro','Adesina','Okeke','Adetola','Okafor','Ajibola','Olaleye','Alade','Olatunji','Alemika','Oyedele','Alozieuwa','Afolabi','Amusan','Aina','Anibaba','Jimoh','Anjorin','Kareem','Arigbabuwo','Lawal','Awosika','Makanjuola','Ayeni','Momoh','Bankole','Nwankwo','Bashir','Nwachukwu','Bello','Obi','Dada','Nwosu','Danjuma','Odeyemi','Ekechukwu','Ogunbiyi','Ezeokafor','Olufemi','Fashola','Olusola','Ganiyu','Olutayo','Hassan','Owolabi','Ibrahimovitch','Popoola','Idrisovitch','Rajiovitch','Igeovitch','Suleimanovitch','Yakubuovitch']

data = []

# Function to generate dates

for i in range(num_users):
    patientID = f"PT-{1000+i}"
    fn = np.random.choice(fnames)
    ln = np.random.choice(lnames)
    fullname = fn + " " + ln
    data.append([patientID, fullname])

# Creating a DataFrame
df = pd.DataFrame(data, columns=['patientID', 'fullName'])

# Saving to CSV
df.to_csv('Fictitious_name__data.csv', index=False)


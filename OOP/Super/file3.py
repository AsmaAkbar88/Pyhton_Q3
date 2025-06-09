class MagicToyError():
    pass
class MagicToyCatalog:


# 🔮 Step 1: __init__ — jab nayi dukan banti hai_____________________________________

    def __init__(self):
        self.toys = {}

# 🏷️ Step 2: __setitem__ — jab toy add karte hain

    def __setitem__(self, name, details):
        self.toys[name] = details

# 🔍 Step 3: __getitem__ — jab toy ki detail chahiye
    def __getitem__(self, name):
        return self.toys.get(name, ("Unknown", "Not in stock"))
    
# catalog = MagicToyCatalog()
# catalog["RoboDog"] = (49.99, "Self-charging robot dog")
# print(catalog["RoboDog"])  #OOUTPUT: (49.99, 'Self-charging robot dog'

# ________________________________________________________________________________________________
    
# 🗑️ Step 4: __delitem__ — jab toy delete karte ho

    def __delitem__(self , name):
        if name in self.toys:
            del self.toys[name]
            print(f"Poof! {name} vanished from the catal")
        else:
            raise MagicToyError(f"✨ {name} doesn't exist in our dimension")

# catalog = MagicToyCatalog()
# catalog["RoboDog"] = ( "RoboDog :",  49.99, "Self-charging robot dog")
# print(catalog["RoboDog"])  #OOUTPUT: ('RoboDog :', 49.99, 'Self-charging robot dog')
# del catalog["RoboDog"]
# print(catalog["FlyingCar"]) #OUTPUT:  ('Unknown', 'Not in stock')
# ____________________________________________________________________________
        
# 🔎 Step 5: __contains__ — check karna toy hai ya nahi


    def __contains__(self, name):
        return name in self.toys


# 🔢 Step 6: __len__ — total kitne toys hain?

    def __len__(self):
        return len(self.toys)
    
# catalog = MagicToyCatalog()
# catalog["RoboDog"] = ( "RoboDog :",  49.99, "Self-charging robot dog")
# print(catalog["RoboDog"])  #OOUTPUT: ('RoboDog :', 49.99, 'Self-charging robot dog')
# catalog.toys["MagicKit"] = (29.95, "150 magic tricks set")

# #contains
# print("MagicKit" in catalog)  #ooutput:   True
# print("RoboDog" in catalog)   #output:    True
# catalog.toys["RoboDog"] = (49.99, "Robot Dog")
# catalog.toys["Doll"] = (49.99, "Doll")
# print(len(catalog))    #OUTPUT:   3

# _____________________________________________________________
    
# # 🔁 Step 7: __iter__ — har toy par loop 


    def __iter__(self):
        return iter(self.toys.items())
    

# catalog = MagicToyCatalog()
# catalog["RoboDog"] = ( "RoboDog :",  49.99, "Self-charging robot dog")
# print(catalog["RoboDog"])  #OOUTPUT: ('RoboDog :', 49.99, 'Self-charging robot dog')
# catalog.toys["MagicKit"] = (29.95, "150 magic tricks set")
# catalog.toys["Doll"] = (29.95, "150 magic tricks set")
# for name, details in catalog:
#     print(name, "=>", details)


# #OUTPUT:   ('RoboDog :', 49.99, 'Self-charging robot dog')
# RoboDog => ('RoboDog :', 49.99, 'Self-charging robot dog')
# MagicKit => (29.95, '150 magic tricks set')
# Doll => (29.95, '150 magic tricks set')


# _____________________________________________________________


# ➕ Step 8: __add__ — 2 dukaane jodna

    def __add__(self, other):
        new_catalog = MagicToyCatalog()
        new_catalog.toys = {**self.toys, **other.toys}
        return new_catalog
# 📝 Step 9: __str__ — print karne pe sundar output


catalog1 = MagicToyCatalog()
catalog2 = MagicToyCatalog()

catalog1.toys["MagicKit"] = (29.95, "150 magic tricks set")
catalog2.toys["Dragon"] = (199.99, "Crystal dragon")

combined = catalog1 + catalog2
print(combined.toys)

#ouput:  {'MagicKit': (29.95, '150 magic tricks set'), 'Dragon': (199.99, 'Crystal dragon')}
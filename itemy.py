class Inventory():
    def __init__(self, max_space, items, gold):
        self.max_space=max_space
        self.items=items
        self.gold=gold

    def show_inventory(self):
        print("You carry {} gold and your inventory space is {}/{} full of items.".format(self.gold,len(self.items),self.max_space))
        #Dopln vypis itemov v inventory...
        # Ak je jeden item viac krat v inventory chces ho vypisat v jednom riadku, priklad:
        #  3 apple 1g 
        #  1 herb  2g
        #  1 magic scroll 10g


    def get_item(self,item):
        quantity=0
        #zisti kolko mas daneho itemu v intentari, ak ziaden tak vrati 0
        return quantity

    def add_item(self, item, quantity):
        #ak sa da, pridaj item ak nie napis, ze sa to neda
        #quantita je zo kolko kopii itemu chces pridat
        #malo by to byt user friendly, ze ak je kvantita 999 ta prida tolko itemov, kolko sa zmesti do ruksaku
        pass

    def remove_item(self, item, quantity):
        #opak add itemu
        pass

    def sell_item(self, item, quantity, price_modif):
        #removne zadani pocet itemov z inventara, ale zaroven ziska money za kazdy predany item
        # price_modif bude napr tak 0.5 co znamena, ze za predane itemy dostavas 50% z ich hodnoty
        pass

    def buy_item(self, item, quantity):
        #prida itemy do inventara ak mas na ne goldy a miesto
        #znova nech je to user friendly ked niekto zavola buy apple 999 tak nech to kupuje jablka dokym jedno z miesta, penazi sa neminie 
        pass

    def sort_by_price(self):
        #zoradi itemy podla hodnoty a vypise ich do konzoly
        #pracujes s listom self.items
        #vzdy ked vypisujes do konzoly tak rozumne vypis aj quantitu itemu, cenu itemu a vahu itemu
        pass

    def sort_by_type(self):
        #zoradi itemy podla typu a vypise nazov typu a potom vsetky, ktore z toho typu mas zvlast do riadku
        pass
  
    def sort_by_rarity(self):
        #tiez vypise pre kazdu raritu najprv nazov rarity a potom vsetky itemy z tej rarity
        pass

    def force_remove(self, x):
        #prinuti hraca odstranit "x" itemov z inventara, napriklad lebo sa mu zmensil max_size
        #chces pouzit input("") aby si ziskal input od hraca
        pass



class Item():
    def __init__(self,name,value,rarity,typ):
        self.name=name #nazov itemu 
        self.value=value #hodnota itemu v goldoch [0-999]
        self.rarity=rarity #rarita itemu ["common", "rare", "legendary"]
        self.typ=typ #typ itemu - [consumable, crafting, scroll, quest]
    

#priklad pre testovanie    
inv = Inventory(10,[],20)

item1 = Item("apple",1,"common","consumable")
item2 = Item("herb",3,"common","crafting")
item3 = Item("magic scroll",10,"rare","scroll")

inv.items.append(item1)
inv.items.append(item1)
inv.items.append(item1)
inv.items.append(item2)
inv.items.append(item3)

inv.show_inventory()
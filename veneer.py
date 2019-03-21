"""

CODECADEMY VENEER PROJECT

"""


class Art:

    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "This painting is made by {}, titled '{}', in the year {}, using {}. The owner of the art is {}, {}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)


class Marketplace:

    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired):
        self.listings.remove(expired)

    def show_listings(self):

        for item in self.listings:
            print(item)


class Client:

    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum

        if self.is_museum:
            self.location =location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):

        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)


    def buy_artwork(self, artwork):

        if artwork.owner is not self:
            art_listing = None
            for item in veneer.listings:
                if item.art == artwork:
                    art_listing = item
                    break

            if art_listing != None:
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)
                print("Art has been sold to {}, located in {}\n".format(self.name, self.location))




class Listing:

    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "The art piece called '{}', is listed for sale for ${} by {}".format(self.art.title, self.price, self.seller.name)




## CLASS INSTANCES ##

veneer = Marketplace()

edytta = Client("Edytta Halpirt", None, False)

moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

## TEST CODES ##

# print(girl_with_mandolin)
# print(edytta)
# print(moma)

#### FOR SELLING ####

edytta.sell_artwork(girl_with_mandolin, 60000)

veneer.show_listings()

print("\n--------------------\n") ### EASIER SEPERATION

#### FOR BUYING ####

moma.buy_artwork(girl_with_mandolin)



##### UPDATES? #####

## Adding wallet ##

"""


class Client:

    def __init__(self, name, location, is_museum, wallet):    #1 ADDED WALLET
        self.name = name
        self.is_museum = is_museum
        
        self.wallet = wallet            #1
        
        if self.is_museum:
            self.location =location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):

        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)


    def buy_artwork(self, artwork):

        if artwork.owner is not self:
            art_listing = None
            for item in veneer.listings:
                if item.art == artwork:
                    art_listing = item
                    break

### FUNCTION WHICH YOU BUY THE ART ###

            if art_listing != None:
            
                if self.wallet >= self. price     #2 to check if wallet is bigger than self.price
            
                art_listing.art.owner = self
                veneer.remove_listing(art_listing)
                print("Art has been sold to {}, located in {}\n".format(self.name, self.location))


#3 ADDED WALLET BALANCES

edytta = Client("Edytta Halpirt", None, False, 15000)   

moma = Client("The MOMA", "New York", True, 20000)



#### FOR SELLING ####

edytta.sell_artwork(girl_with_mandolin, 60000)

veneer.show_listings()

#### FOR BUYING ####

moma.buy_artwork(girl_with_mandolin)


"""










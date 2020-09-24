class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return (f"{self.artist}.\"{self.title}\". {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}")


class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    #return self.listings

  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    #return self.listings

  def show_listing(self):
    for listings in self.listings:
      print(listings)

veneer = Marketplace()


class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)


class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return (f"This art work is called {self.art.title} and the price is {self.price}")

edytta = Client("Edytta Halpirt", location= "Private Collection", is_museum= False)


moma = Client("The MOMA", location= "New York", is_museum= True)

girl_with_mandolin = Art("Picasso, Pablo.", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas.", 1910, edytta)

print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

veneer.show_listing()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

veneer.show_listing()

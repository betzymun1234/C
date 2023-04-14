cake = int ( input ('Enter a number 1- 14 to get your cake!:'))
def cakePrinter(cake):
  switcher = {
    1: "Strawberry shortcake, yum!",
    2: "Chocolate fudge cake",
    3: "Chocolate lava cake", 
    4: "Vanilla tres leches cake!",
    5: "Red velvet cake drizzled with some dark chocolate",
    6: "Strawberry Cheescake",
    7: "Devil's Food cake",
    8: "Spongecake! ",
    9: "Oreo ice cream cake"
  }
  print(switcher.get( cake, " No cake!?")) #default
cakePrinter( cake )
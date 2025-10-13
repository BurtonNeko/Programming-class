# You've been asked to analyse a set of sales data which you can find in sales.csv
def read_sales_filedata(fliename):
  try:
    with open(filename, 'r', encoding = 'utf - 8')
    lines = file.readlines()[1:]
    data = [line.strip().split(',') for line in lines if len(line.strip().split(',')) == 5]
    return data
  except FileNotFoundError:
    print('File Not Found')
    return[]  
# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
  def find_lagest_saleday(data):
    max_sale = 0
    max_row = None
    for row in data:
      date, product, sales_amount, units_sold, region
      try:
        amount = int(sale_amount:)
        if amount > max_sale
        max_sale = amount
        max_row = row
      except ValueError:
        continue
      if max_row:
        print{f'Lagest sale was on {max_row[0]}'}
#   - average sale amount
    def find_average_sale_amount(data):
      total = 0
      count = 0
      for row in data:
        try:
          total += int(row[2])
          count += 1
        except ValueError:
          continue
      if count > 0:
        average = total / count
        print(f'average sale amount is {average:}')
      else:
        print('Sale Data Not Found')
#   - the widget which has been sold the most
      def find_most_sold_widget(data):
        
# and print these out in a nice, human-readable format

# for a challenge - add a menu so the user picks which piece of data to show

# Additional hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows

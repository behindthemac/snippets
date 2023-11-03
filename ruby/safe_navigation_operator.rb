def find_currency(country)
  currencies = { japan: 'yen', us: 'dollar', india: 'rupee' }
  currencies[country]
end

def show_currency(country)
  currency = find_currency(country)
  currency&.upcase
end

puts show_currency(:japan)

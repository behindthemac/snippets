text = '私の誕生日は2112年9月3日です。'

# Example 1
m = /(?<year>\d+)年(?<month>\d+)月(?<day>\d+)日/.match(text)
puts "#{m[:year]}/#{m[:month]}/#{m[:day]}"

# Example 2
if /(?<year>\d+)年(?<month>\d+)月(?<day>\d+)日/ =~ text
  puts "#{year}/#{month}/#{day}"
end

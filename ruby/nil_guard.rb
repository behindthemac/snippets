# When a is nil
a = nil
a ||= 10
puts a #=> 10

# When a is not nil
a = 1
a ||= 10
puts a #=> 1

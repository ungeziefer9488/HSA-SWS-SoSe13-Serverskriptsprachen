#!/usr/bin/env ruby

if __FILE__ == $0
    if 1 > 2
        puts "1 > 2"
    elsif 1 < 2
        puts "1 < 2"
    else
        puts "This should never happen!"
    end
end
